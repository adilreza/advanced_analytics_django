from django.db import models


# customized function

def upload_path(instance, filename):
    return '/'.join(['covers', str(instance.title), filename])

# Create your models here.


class myModel(models.Model):
    data1 = models.CharField(max_length=400)
    data2 = models.CharField(max_length=300)


class withoutMigrate(models.Model):
    data3 = models.CharField(max_length=400)
    data4 = models.CharField(max_length=500)


class Book(models.Model):
    title = models.CharField(max_length=300)
    cover = models.ImageField(blank=True, null=True, upload_to=upload_path)
