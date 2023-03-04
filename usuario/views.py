from django.shortcuts import render
from rest_framework import generics
from .models import CustomUser as User
from .serializers import UserSerializer

# Create your views here.

class ListUsers(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    
