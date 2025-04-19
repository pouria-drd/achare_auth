from django.core.validators import RegexValidator

# ----------------------------------
# Iranian Phone Number Validator
# Only 09xxxxxxxxx format is valid
# ----------------------------------

iran_phone_validator = RegexValidator(
    regex=r"^09\d{9}$",
    message="Enter a valid Iranian phone number starting with 09 (e.g., 09123456789).",
    code="invalid_phone",
)
