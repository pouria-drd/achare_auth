from accounts.models import UserModel
from rest_framework import serializers


class LoginSerializer(serializers.ModelSerializer):
    """
    Serializer for login attempts.
    """

    phoneNumber = serializers.CharField(
        required=True,
        min_length=11,
        max_length=11,
        error_messages={
            "required": "شماره همراه الزامی است.",
            "blank": "شماره همراه نمی‌تواند خالی باشد.",
            "min_length": "شماره همراه باید حداقل 11 کاراکتر باشد.",
            "max_length": "شماره همراه باید حداکثر 11 کاراکتر باشد.",
        },
    )
    password = serializers.CharField(
        required=True,
        write_only=True,
        error_messages={
            "required": "رمز عبور الزامی است.",
            "blank": "رمز عبور نمی‌تواند خالی باشد.",
        },
    )

    class Meta:
        model = UserModel
        fields = ["phoneNumber", "password"]
