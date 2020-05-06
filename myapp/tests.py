from django.test import TestCase
from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase
from rest_framework import status
import json
from .models import myModel
# Create your tests here.

class MyModelTestCase(APITestCase):
    def setUp(self):
        myModel.objects.create(data1="hasan",data2="vai")

    
    def test_mymodel_tester(self):
        data = {'data1':"this is new data", "data2":"data"}
        response = self.client.post('/test/api/mymodel/', data)
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_get_data(self):
        myd = {"id":1,"data1":"hasan","data2":"vai"}
        response = self.client.get('/test/api/mymodel/1/')
        print("--------------")
        get_data = json.loads(response.content)
        print(json.loads(response.content))
        print("--------------")
        self.assertEqual(get_data, myd)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
   
