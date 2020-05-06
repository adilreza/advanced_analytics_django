from django.urls import path
from rest_framework import routers
from .restapi import MyModelViewset

routter1 = routers.DefaultRouter()

routter1.register('api/mymodel',MyModelViewset)

urlpatterns = routter1.urls
