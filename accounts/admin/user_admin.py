from accounts.models import UserModel
from django.contrib import admin, messages
from django.contrib.auth.admin import UserAdmin


@admin.register(UserModel)
class UserAdmin(UserAdmin):
    model = UserModel

    list_display = [
        "phone_number",
        "first_name",
        "last_name",
        "email",
        "is_active",
        "is_staff",
        "is_superuser",
        "last_login",
        "created_at",
    ]
    search_fields = ["phone_number", "email", "first_name", "last_name"]

    # Optimized ordering (avoid non-sortable fields)
    ordering = ["phone_number", "email", "first_name", "last_name"]

    readonly_fields = ["id", "last_login", "updated_at", "created_at"]

    fieldsets = (
        (None, {"fields": ("phone_number", "password")}),
        (
            "Personal info",
            {"fields": ("first_name", "last_name", "email")},
        ),
        (
            "Permissions",
            {"fields": ("is_active", "is_staff", "is_superuser", "user_permissions")},
        ),
        ("Important dates", {"fields": ("last_login", "created_at")}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "phone_number",
                    "email",
                    "password1",
                    "password2",
                ),
            },
        ),
    )

    # Actions for activating and deactivating users
    actions = ["activate_users", "deactivate_users"]

    @admin.action(description="Activate selected users")
    def activate_users(self, request, queryset):
        updated_count = queryset.update(is_active=True)
        self.message_user(
            request, f"{updated_count} user(s) activated.", messages.SUCCESS
        )

    @admin.action(description="Deactivate selected users")
    def deactivate_users(self, request, queryset):
        updated_count = queryset.update(is_active=False)
        self.message_user(
            request, f"{updated_count} user(s) deactivated.", messages.WARNING
        )
