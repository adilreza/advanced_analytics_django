from django.db import models

# Create your models here.

class myModel(models.Model):
    data1 = models.CharField(max_length=400)
    data2 = models.CharField(max_length=300)
    