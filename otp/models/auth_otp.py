from django.db import models
from .base_otp_model import BaseOTPModel


class AuthOTPModel(BaseOTPModel):
    """
    Model for Auth OTP codes.
    """

    # IP address of the user who generated the OTP code.
    ip_address = models.GenericIPAddressField()
    # Phone number of the user who generated the OTP code.
    phone_number = models.CharField(max_length=13, null=True, blank=True)
    # Blocked until date.
    blocked_until = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Auth OTP code"
        verbose_name_plural = "Auth OTP codes"

    def __str__(self) -> str:
        return f"Login OTP for {self.phone_number}"
