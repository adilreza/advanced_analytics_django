import pytest
import json
import math

@pytest.mark.mathing
def test_sqrt():
    num = 25
    assert math.sqrt(num) == 5

#if any error occured to this method the rest of function will not excute 
@pytest.mark.mathing
def testsquare():
   num = 7
   assert 7*7 == 49

def testequality():
   #assert 10 == 11
   assert 10 == 10