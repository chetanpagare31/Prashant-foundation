from django.shortcuts import render

from django.contrib.auth.models import User

from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError

class UserView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self,request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset,many=True)
        return Response(serializer.data)


class RegisterUserView(APIView):
    def post(self,request):
        serializer = RegisterSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class LoginUserView(APIView):
    def post(self,request,*args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email'].lower()
            password = serializer.validated_data['password']
            try:
                user = User.objects.get(email=email)
                if user.check_password(password):
                    refresh = RefreshToken.for_user(user)
                    response_data = {
                        'refresh': str(refresh),
                        'access': str(refresh.access_token),
                        'user': UserSerializer(user).data
                    }
                    return Response(response_data,status=status.HTTP_200_OK)
                else:
                    return Response("Invalid credentials", status=status.HTTP_401_UNAUTHORIZED)
            except User.DoesNotExist:
                return Response({'error':'Invalid email'},status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)




class RevokeTokenView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"detail": "Refresh token revoked."},status=status.HTTP_205_RESET_CONTENT)
        except KeyError:
            return Response({"detail": "Refresh token is required."}, status=status.HTTP_400_BAD_REQUEST)
        except TokenError:
            return Response({"detail": "Invalid token."}, status=status.HTTP_400_BAD_REQUEST)