from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializer import ProductSerializer
from rest_framework import status

# Create your views here.
def home(request):
    return render(request,'home/home.html')

@api_view(['GET','POST'])
def product(request):
    if request.method == 'GET':
        list = Product.objects.all()
        serializer = ProductSerializer(list,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status= status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
