from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .models import User
from .serializers import UserSerializer

class SignupView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = RefreshToken.for_user(user)
            return Response({'token': str(token.access_token)}, status=201)
        return Response(serializer.errors, status=400)

class LoginView(APIView):
    def post(self, request):
        user = authenticate(username=request.data['username'], password=request.data['password'])
        if user:
            token = RefreshToken.for_user(user)
            return Response({'token': str(token.access_token)}, status=200)
        return Response({'error': 'Invalid credentials'}, status=400)

class AdminLoginView(APIView):
    def post(self, request):
        user = authenticate(username=request.data['username'], password=request.data['password'])
        if user and user.is_admin:
            token = RefreshToken.for_user(user)
            return Response({'admin_token': str(token.access_token)}, status=200)
        return Response({'error': 'Unauthorized'}, status=403)
