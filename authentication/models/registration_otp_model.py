from django.db import models
from otp.models import BaseOTPModel


class RegistrationOTPModel(BaseOTPModel):
    """
    Model for user registration OTP codes.
    """

    # Phone number of the user who generated the OTP code.
    phone_number = models.CharField(max_length=11, null=True, blank=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Registration OTP code"
        verbose_name_plural = "Registration OTP codes"

    def __str__(self) -> str:
        return f"Registration OTP for {self.phone_number}"
