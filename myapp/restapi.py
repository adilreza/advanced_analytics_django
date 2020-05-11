from rest_framework import viewsets
from django.http import HttpResponse
from django.core import serializers


#all model
from .models import myModel
from .models import withoutMigrate
from .models import Book


#serializer
from .serializers import MyModelSerializer
from .serializers import WithoutMigratSerializer
from .serializers import BookSerializer


class MyModelViewset(viewsets.ModelViewSet):
    queryset = myModel.objects.all()
    serializer_class = MyModelSerializer


class withoutMigrateViewSet(viewsets.ModelViewSet):
    queryset = withoutMigrate.objects.all()
    serializer_class = WithoutMigratSerializer

    def post(self, request, *args, **kwargs):
        data3 = request.data['data3']
        data4 = request.data['data4']
        data4= data4 + " customized"
        print(data4+data4)
        withoutMigrate.objects.create(data3 = data3, data4 = data4)
        return super().create(request)
        # return HttpResponse({'message':"succefully saved"}, status=200)


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer