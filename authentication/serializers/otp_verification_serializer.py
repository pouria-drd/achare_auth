from rest_framework import serializers


class OTPVerificationSerializer(serializers.Serializer):
    otpId = serializers.UUIDField(
        required=True,
        error_messages={
            "required": "شناسه ارسال شده است.",
            "blank": "شناسه ارسال شده نمی‌تواند خالی باشد.",
        },
    )

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
    otpCode = serializers.CharField(
        required=True,
        min_length=6,
        max_length=6,
        error_messages={
            "required": "کد ارسال شده است.",
            "blank": "کد ارسال شده نمی‌تواند خالی باشد.",
            "min_length": "کد ارسال شده باید حداقل 6 کاراکتر باشد.",
            "max_length": "کد ارسال شده باید حداکثر 6 کاراکتر باشد.",
        },
    )
