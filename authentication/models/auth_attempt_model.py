import uuid
from django.db import models
from django.utils import timezone

auth_type_choices = (
    ("entry", "Entry"),
    ("login", "Login"),
    ("otp_verify", "OTP Verify"),
    ("registration", "Registration"),
)


class AuthAttemptModel(models.Model):
    """
    Model for user authentication attempts.
    """

    # Unique ID for the authentication attempt
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    auth_type = models.CharField(max_length=12, choices=auth_type_choices)
    # IP address of the user who requested the OTP code.
    ip_address = models.GenericIPAddressField()
    # Phone number of the user who requested the OTP code.
    phone_number = models.CharField(max_length=11, null=True, blank=True)
    # Number of authentication attempts
    count = models.PositiveIntegerField(default=0)
    # Whether the attempt has been used
    is_used = models.BooleanField(default=False)
    # Blocked until date.
    blocked_until = models.DateTimeField(null=True, blank=True)
    # Timestamps for OTP creation and last update
    created_at = models.DateTimeField(auto_now_add=True)
    last_attempted = models.DateTimeField(auto_now=True)

    def is_blocked(self):
        if self.blocked_until and timezone.now() < self.blocked_until:
            return True
        return False

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Auth attempt"
        verbose_name_plural = "Auth attempts"

    def __str__(self) -> str:
        return f"{self.auth_type} attempt for {self.phone_number}"
