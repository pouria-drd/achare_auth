from django.contrib import admin
from otp.models import AuthOTPModel


@admin.register(AuthOTPModel)
class AuthOTPAdmin(admin.ModelAdmin):

    list_display = (
        "phone_number",
        "ip_address",
        "blocked_until",
        # bools
        "is_verified",
        "is_active",
        "is_expired",
        # ints
        "attempts",
        "max_attempts",
        # datetimes
        "last_attempted",
        "created_at",
        "expires_at",
    )
    readonly_fields = (
        "code",
        # bools
        "is_verified",
        "is_active",
        "is_expired",
        # ints
        "attempts",
        "max_attempts",
        # datetimes
        "last_attempted",
        "created_at",
        "expires_at",
    )
    search_fields = ("phone_number", "ip_address")
    list_filter = ("phone_number", "ip_address", "is_active", "is_verified")

    def is_expired(self, obj):
        """Display whether the OTP is expired."""
        return obj.is_expired()

    is_expired.boolean = True
    is_expired.short_description = "Expired"

    def has_change_permission(self, request, obj=None):
        """Restrict edit permissions for the OTP code."""
        if obj:
            return False  # Prevent editing of OTP codes
        return super().has_change_permission(request, obj)
