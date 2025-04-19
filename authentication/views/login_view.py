from datetime import timedelta
from django.utils import timezone
from django.contrib.auth import authenticate

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from authentication.utils import get_client_ip
from authentication.serializers import LoginSerializer
from authentication.models import AuthAttemptModel as LoginAttempt


class LoginView(APIView):
    http_method_names = ["post"]
    permission_classes = [AllowAny]

    def post(self, request: Request) -> Response:
        # Validate the request data
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Get the validated data from the serializer
        password = serializer.validated_data["password"]
        phone_number = serializer.validated_data["phoneNumber"]
        # Authenticate the user using the phone number and password
        user = authenticate(phone_number=phone_number, password=password)
        # Get the client IP address
        client_ip = get_client_ip(request)
        # Get user's login attempt
        attempt, _ = LoginAttempt.objects.get_or_create(
            phone_number=phone_number,
            ip_address=client_ip,
            auth_type="login",
            is_used=False,
        )
        # Check if the user is authenticated
        if not user:
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

            return Response(
                {"detail": "رمز عبور یا شماره همراه اشتباه است."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        # else, the user is authenticated

        # Check if the user is active
        if not user.is_active:
            return Response(
                {"detail": "حساب کاربری شما فعال نیست."},
                status=status.HTTP_403_FORBIDDEN,
            )

        attempt.is_used = True
        attempt.save()

        # TODO: Token generation

        return Response({"detail": "ورود موفقیت‌آمیز بود."}, status=status.HTTP_200_OK)
