from rest_framework import serializers
from myapp.models import myModel



class MyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = myModel
        fields = '__all__'