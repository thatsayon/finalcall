from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import views, status

from .serializers import (
    LoginSerializer,
    RegistrationSerializer
)

class LoginView(APIView):

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(
            {
                "msg": "working",
            },
            status=status.HTTP_200_OK
        )

class RegistrationView(APIView):

    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(
            {
                "msg": "working"
            },
            status=status.HTTP_200_OK
        )
