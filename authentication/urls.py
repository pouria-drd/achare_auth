from django.urls import path
from authentication.views import AuthEntryView, LoginView

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("auth_entry/", AuthEntryView.as_view(), name="auth_entry"),
]
