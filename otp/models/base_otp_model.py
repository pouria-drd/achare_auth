import uuid
import hashlib
from django.db import models


class BaseOTPModel(models.Model):
    """
    Base model for OTP codes.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # Store hashed version of OTP
    code = models.CharField(max_length=256)
    # Whether the OTP has been used
    is_used = models.BooleanField(default=False)
    # Number of verification attempts
    attempts = models.PositiveIntegerField(default=0)
    # Max allowed attempts
    max_attempts = models.PositiveIntegerField(default=3)
    # Timestamps for OTP creation and last update
    created_at = models.DateTimeField(auto_now_add=True)
    last_attempted = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = "-created_at"
        verbose_name = "Base OTP code"
        verbose_name_plural = "Base OTP codes"

    def has_attempts_left(self) -> bool:
        """Check if the OTP has attempts left."""
        result: bool = self.attempts < self.max_attempts
        return result

    def hash_otp(self, otp: str) -> str:
        """Hash the OTP code using SHA-256."""
        hashed_otp: str = hashlib.sha256(otp.encode()).hexdigest()
        return hashed_otp

    def check_otp(self, otp_code) -> bool:
        """Compare the OTP code with the stored OTP code."""
        result: bool = self.hash_otp(otp_code) == self.code
        return result

    def save(self, *args, **kwargs):
        # Check if the OTP has attempts left
        if not self.has_attempts_left():
            raise ValueError("OTP has reached its maximum attempts")

        if not self.code:
            raise ValueError("OTP code cannot be empty")

        # Hash the OTP code
        otp_code: str = self.code
        self.code = self.hash_otp(otp_code)

        super().save(*args, **kwargs)
