import re
from rest_framework import serializers


class PhoneNumberSerializer(serializers.Serializer):
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

    def validate_phoneNumber(self, value):
        # Advanced Regex Validation for Iranian Phone Number
        phone_regex = r"^09\d{9}$"
        if not re.match(phone_regex, value):
            raise serializers.ValidationError("شماهر همراه معتبر نیست.")

        return value
