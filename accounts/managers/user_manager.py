from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    """
    Custom manager for the UserModel, handling user and superuser creation.
    """

    def create_user(self, phone_number=None, password=None, **extra_fields):
        """
        Creates and returns a regular user.
        """
        # Ensure that the user has a phone_number
        if not phone_number:
            raise ValueError("Users must have a phone_number")

        # Ensure that the user has a password
        if not password:
            raise ValueError("Users must have a password")

        # Create the user instance with the provided details
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)  # Hash the password before saving
        user.save(using=self._db)  # Save the user to the database

        return user

    def create_superuser(self, phone_number=None, password=None, **extra_fields):
        """
        Creates and returns a superuser with all permissions.
        """
        # Set the phone number to None by default if not provided
        if not phone_number:
            phone_number = None

        user = self.create_user(
            phone_number=phone_number, password=password, **extra_fields
        )

        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if not extra_fields["is_staff"]:
            raise ValueError("Superuser must have is_staff=True.")

        if not extra_fields["is_superuser"]:
            raise ValueError("Superuser must have is_superuser=True.")

        user.save(using=self._db)

        return user
