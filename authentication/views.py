from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import AllowAny
from .serializers import RegistrationSerializer, LoginSerializer, UserListSerializer
from .models import User
class RegistrationAPIView(APIView):
    print("************registerview")
    permission_classes = (AllowAny,)

    serializer_class = RegistrationSerializer
    def post(self, request):
        user = request.data.get('user', {})
        if not user:
            user = {
                "username": request.data.get('username'),
                "password": request.data.get('password')
            }
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class LoginAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer
    def post(self, request):
        user = request.data.get('user', {})
        # this is base case if user is not created:
        if not user:
            user = {
                "username": request.data.get('username'),
                "password": request.data.get('password'),
            }
        serializer = self.serializer_class(data=user)
        # raise an error if it doesn't go right
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
