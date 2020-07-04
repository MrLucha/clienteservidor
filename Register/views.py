from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,generics
from Register.serializer import UserSerializer

# Create your views here.
class SaveRegister(ObtainAuthToken,APIView):
    def get (self,request, format = None):
        queryset = User.objects.all() 
        serializer = UserSerializer(queryset, many = True)
        return Response(serializer.data)
    
    def post(self,request, format = None):
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            user = serializer.save()
            datas = serializer.data     
            token, created = Token.objects.get_or_create(user=user)
            return Response (datas)
        else :
            return Response (serializer.errors)
           