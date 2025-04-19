from rest_framework.request import Request
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from authentication.serializers import RegisterUserSerializer


class RegisterView(generics.CreateAPIView):
    http_method_names = ["post"]
    permission_classes = [AllowAny]
    serializer_class = RegisterUserSerializer

    def post(self, request: Request, *args, **kwargs):
        # Call the serializer to validate and create the user
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Save user
            serializer.save()

            return Response(
                {"message": "اطلاعات شما با موفقیت ثبت شد."},
                status=status.HTTP_201_CREATED,
            )

        # Return validation errors
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
