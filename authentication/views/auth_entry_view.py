from datetime import timedelta
from django.utils import timezone
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from accounts.models import UserModel
from otp.utils import generate_otp_code
from authentication.utils import get_client_ip
from authentication.serializers import PhoneNumberSerializer
from authentication.models import RegistrationOTPModel as OTP
from authentication.models import AuthAttemptModel as EntryAttempt


class AuthEntryView(APIView):
    http_method_names = ["post"]
    permission_classes = [AllowAny]

    def post(self, request: Request) -> Response:
        # Validate the request data
        serializer = PhoneNumberSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        phone_number = serializer.validated_data["phoneNumber"]

        # Get the client IP address
        client_ip = get_client_ip(request)
        # Get user's login attempt
        attempt, _ = EntryAttempt.objects.get_or_create(
            phone_number=phone_number,
            ip_address=client_ip,
            auth_type="entry",
            is_used=False,
        )

        # Check if the login attempt has been blocked
        if attempt.is_blocked():
            # Calculate the remaining time in minutes
            remaining = int(
                (attempt.blocked_until - timezone.now()).total_seconds() // 60
            )
            return Response(
                {
                    "detail": f"درحال حاضر نمی‌توانید وارد شوید، {remaining} دقیقه دیگر تلاش کنید."
                },
                status=status.HTTP_403_FORBIDDEN,
            )

        # Check if the login attempt has reached its maximum attempts
        attempt.count += 1
        if attempt.count >= 3:
            attempt.blocked_until = timezone.now() + timedelta(hours=1)
            attempt.count = 0

        attempt.save()

        # Check if the phone number is already registered
        user = UserModel.objects.filter(phone_number=phone_number).first()
        if user:
            return Response(
                {"detail": "شماره همراه قبلا ثبت شده است.", "next": "confirm-password"},
                status=status.HTTP_200_OK,
            )

        otp_code = generate_otp_code()
        otp = OTP.objects.create(phone_number=phone_number, code=otp_code)

        # Send the OTP code to the user's phone number (simulated)
        print(f"کد تایید برای {phone_number}: {otp_code}")

        return Response(
            {
                "detail": "کد ارسال شد.",
                "otpInfo": {
                    "id": otp.id,
                },
                "next": "confirm-otp",
            },
            status=status.HTTP_200_OK,
        )
