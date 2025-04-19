from django.contrib import admin
from authentication.models import RegistrationOTPModel


@admin.register(RegistrationOTPModel)
class RegistrationOTPAdmin(admin.ModelAdmin):
    list_display = (
        "phone_number",
        "code",
        "attempts",
        "max_attempts",
        "is_used",
        # datetimes
        "created_at",
        "last_attempted",
    )
    readonly_fields = (
        "code",
        "attempts",
        "max_attempts",
        "is_used",
        # datetimes
        "created_at",
        "last_attempted",
    )
    search_fields = ("phone_number", "code")
    list_filter = ("phone_number", "is_used")

    def is_used(self, obj):
        """Display whether the OTP is used."""
        return obj.is_used

    is_used.boolean = True
    is_used.short_description = "Used"
