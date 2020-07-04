from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,generics

from django.http import Http404
from django.shortcuts import get_object_or_404

# Create your views here.

#Importacion de modelo
from Example1.models import ExampleModel

#Importacion de serializer
from Example1.serializer import Example1Serializer

class ExampleList(APIView):
    def get(self,request,format=None):
        print("GET")
        queryset=ExampleModel.objects.all()
        serializer=Example1Serializer(queryset,many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        serializer=Example1Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            datas=serializer.data
            return Response(datas)

class ExampleDetail(APIView):
    def get_object(self,id):
        try:
            return ExampleModel.objects.get(pk=id)
        except ExampleModel.DoesNotExist:
            return 404

    def get(self,request,id,format=None):
        print("GET Detail")
        example1=self.get_object(id)
        if example1==404:
            return Response("No existen datos")
        serializer=Example1Serializer(example1)
        return Response(serializer.data)


class ExampleUpdate(APIView):
    def get_object(self,id):
        try:
            return ExampleModel.objects.get(pk=id)
        except ExampleModel.DoesNotExist:
            return 404

    def put(self,request,id,format=None):
        try:
            model=ExampleModel.objects.get(pk=id)
        except ExampleModel.DoesNotExist:
            return Response(f'Usuario con el id {id} no existe')
        #example1=self.get_object(id)
        serializer=Example1Serializer(model,data=request.data)
        if serializer.is_valid():
            serializer.save()
            datas=serializer.data
            return Response(datas)
        return Response(serializer.errors)
        