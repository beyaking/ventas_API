from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from .models import Product 
from .serializers import ProductSerializer
from rest_framework.response import Response

# Create your views here.

class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductCreate(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductView(APIView):

    def get(self, request, *args):
        data = Product.objects.all()
        serializer = ProductSerializer(data,many=True)
        results = serializer.data
        return Response(results)

    
