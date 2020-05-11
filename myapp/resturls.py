from django.urls import path
from rest_framework import routers
from .restapi import MyModelViewset
from .restapi import withoutMigrateViewSet
from .restapi import BookViewSet

routter1 = routers.DefaultRouter()

routter1.register('api/mymodel',MyModelViewset)
routter1.register('api/without',withoutMigrateViewSet)
routter1.register('api/book', BookViewSet)

urlpatterns = routter1.urls
