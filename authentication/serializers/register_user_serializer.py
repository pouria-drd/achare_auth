import re
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password

from accounts.models import UserModel


class RegisterUserSerializer(serializers.Serializer):
    email = serializers.EmailField(required=False)

    firstName = serializers.CharField(
        required=False,
        min_length=3,
        max_length=30,
        error_messages={
            "required": "نام الزامی است.",
            "blank": "نام نمی‌تواند خالی باشد.",
            "min_length": "نام باید حداقل 3 کاراکتر باشد.",
            "max_length": "نام باید حداکثر 30 کاراکتر باشد.",
        },
    )

    lastName = serializers.CharField(
        required=False,
        min_length=3,
        max_length=30,
        error_messages={
            "required": "نام خانوادگی الزامی است.",
            "blank": "نام خانوادگی نمی‌تواند خالی باشد.",
            "min_length": "نام خانوادگی باید حداقل 3 کاراکتر باشد.",
            "max_length": "نام خانوادگی باید حداکثر 30 کاراکتر باشد.",
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

    password = serializers.CharField(
        required=True,
        write_only=True,
        error_messages={
            "required": "رمز عبور الزامی است.",
            "blank": "رمز عبور نمی‌تواند خالی باشد.",
        },
    )

    confirmPassword = serializers.CharField(
        write_only=True,
        required=True,
        error_messages={
            "required": "تکرار رمز عبور الزامی است.",
            "blank": "تکرار رمز عبور نمی‌تواند خالی باشد.",
        },
    )

    def validate_phoneNumber(self, value):
        # Advanced Regex Validation for Iranian Phone Number
        phone_regex = r"^09\d{9}$"
        if not re.match(phone_regex, value):
            raise serializers.ValidationError(
                "شماره تلفن باید یک شماره تلفن معتبر ایرانی باشد"
            )

        # Check if phoneNumber is unique
        if UserModel.objects.filter(phone_number=value).exists():
            raise serializers.ValidationError("این شماره همراه قبلاً ثبت شده است.")

        return value

    def validate_email(self, value):
        # Check if email is unique
        if UserModel.objects.filter(email=value).exists():
            raise serializers.ValidationError("این ایمیل قبلاً ثبت شده است.")

        return value

    def validate(self, data):
        # Password confirmation check
        if data["password"] != data["confirmPassword"]:
            raise ValidationError(
                {"confirmPassword": "رمز عبور و تایید رمز عبور باید یکسان باشند"}
            )
        validate_password(data["password"])
        return data

    def create(self, validated_data):
        # Remove the confirmPassword field from validated_data as it is not used for user creation
        validated_data.pop("confirmPassword", None)

        # Create the user
        user = UserModel.objects.create_user(
            phone_number=validated_data["phoneNumber"],
            password=validated_data["password"],
            first_name=validated_data.get("firstName", ""),
            last_name=validated_data.get("lastName", ""),
            email=validated_data.get("email", ""),
        )

        return user
