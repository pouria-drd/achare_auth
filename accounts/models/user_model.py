import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from accounts.managers import UserManager
from accounts.validators import iran_phone_validator


class UserModel(AbstractBaseUser, PermissionsMixin):
    """
    Custom user model that replaces Django's default user model.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # Email is optional for user creation
    email = models.EmailField(
        unique=True,
        blank=True,  # Email is optional
        null=True,
        help_text="Enter a valid email address.",
    )

    # Phone number is required for user creation
    phone_number = models.CharField(
        max_length=11,
        unique=True,
        blank=False,  # Phone number is required
        null=False,
        validators=[iran_phone_validator],  # Apply phone number validator
        help_text="Enter a valid Iranian phone number (e.g., 09123456789).",
    )

    # Optional last name field, can be left blank or set to null.
    last_name = models.CharField(max_length=30, blank=True, null=True)

    # Optional first name field, can be left blank or set to null.
    first_name = models.CharField(max_length=30, blank=True, null=True)

    # Boolean flags for account status
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # Attach the custom manager
    objects = UserManager()

    # Set the USERNAME_FIELD to 'phone_number' to use the phone number as the username
    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = []

    # Timestamps for user creation and last update
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        Meta class for the UserModel.
        """

        verbose_name = "user"
        verbose_name_plural = "users"
        ordering = ("-created_at",)

    def __str__(self):
        """
        String representation of the user.
        """
        return self.phone_number

    def get_full_name(self):
        """Returns the user's full name or an empty string if missing."""
        return " ".join(filter(None, [self.first_name, self.last_name])) or ""
