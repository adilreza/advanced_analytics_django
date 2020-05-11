from rest_framework import serializers
from myapp.models import myModel
from .models import withoutMigrate
from .models import Book



class MyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = myModel
        fields = '__all__'

class WithoutMigratSerializer(serializers.ModelSerializer):
    class Meta:
        model = withoutMigrate
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'