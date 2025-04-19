from datetime import timedelta
from django.utils import timezone
from django.contrib.auth import authenticate

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from authentication.utils import get_client_ip
from authentication.serializers import LoginSerializer
from authentication.models import AuthAttemptModel


class AuthEntryView(APIView):
    pass
