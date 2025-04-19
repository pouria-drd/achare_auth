from django.contrib import admin
from authentication.models import AuthAttemptModel


@admin.register(AuthAttemptModel)
class AuthAttemptAdmin(admin.ModelAdmin):
    list_display = (
        "phone_number",
        "ip_address",
        "auth_type",
        "blocked_until",
        # bools
        "is_blocked",
        # ints
        "count",
        # datetimes
        "last_attempted",
        "created_at",
    )
    readonly_fields = (
        "id",
        "phone_number",
        "ip_address",
        "auth_type",
        # bools
        "is_blocked",
        # ints
        "count",
        # datetimes
        "last_attempted",
        "created_at",
    )
    search_fields = ("phone_number", "ip_address")
    list_filter = ("phone_number", "ip_address", "auth_type")

    def is_blocked(self, obj):
        """Display whether the attempt is blocked."""
        return obj.is_blocked()

    is_blocked.boolean = True
    is_blocked.short_description = "Blocked"
