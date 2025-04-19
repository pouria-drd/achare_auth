from datetime import timedelta
from django.utils import timezone
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from authentication.utils import get_client_ip
from authentication.models import RegistrationOTPModel as OTP
from authentication.serializers import OTPVerificationSerializer
from authentication.models import AuthAttemptModel as VerifyAttempt


class VerifyOTPView(APIView):
    http_method_names = ["post"]
    permission_classes = [AllowAny]

    def post(self, request: Request) -> Response:
        serializer = OTPVerificationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        client_ip = get_client_ip(request)
        otp_id = serializer.validated_data["otpId"]
        otp_code = serializer.validated_data["otpCode"]
        phone_number = serializer.validated_data["phoneNumber"]

        attempt, _ = VerifyAttempt.objects.get_or_create(
            ip_address=client_ip, phone_number=phone_number, auth_type="otp_verify"
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

        otp_obj = (
            OTP.objects.filter(id=otp_id, phone_number=phone_number, is_used=False)
            .order_by("-created_at")
            .first()
        )

        if not otp_obj or not otp_obj.check_otp(otp_code):
            # Verify OTP code is invalid
            attempt.count += 1
            if attempt.count >= 3:
                attempt.blocked_until = timezone.now() + timedelta(hours=1)
                attempt.count = 0
            attempt.save()
            return Response({"detail": "کد اشتباه است."}, status=400)

        otp_obj.is_used = True
        otp_obj.save()

        return Response(
            {
                "detail": "کد تایید شد، لطفا ادامه ثبت نام را انجام دهید.",
                "next": "user-registration",
            }
        )
