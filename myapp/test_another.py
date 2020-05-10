import pytest
import json
import math
import requests
from django.test import TestCase
from rest_framework import status



def test_sqrt():
   num = 25
   assert math.sqrt(num) == 5

   #if any error occured to this method the rest of function will not excute 
def testsquare():
   num = 7
   assert 7*7 == 49

def testequality():
   #assert 10 == 11
   assert 10 == 10