from rest_framework import viewsets, permissions
from rest_framework import generics
from django.http import JsonResponse
from django.http import HttpResponse
from django.core import serializers
import json


#all model 
from .models import myModel

#serializer 
from .serializers import MyModelSerializer



class MyModelViewset(viewsets.ModelViewSet):
    queryset = myModel.objects.all()
    serializer_class = MyModelSerializer