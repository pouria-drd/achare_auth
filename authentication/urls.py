from django.urls import path
from authentication.views import AuthEntryView, LoginView, RegisterView, VerifyOTPView

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("register/", RegisterView.as_view(), name="register"),
    path("auth_entry/", AuthEntryView.as_view(), name="auth_entry"),
    path("verify_otp/", VerifyOTPView.as_view(), name="verify_otp"),
]
