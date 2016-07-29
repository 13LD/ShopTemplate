from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    quantity = models.IntegerField(default=0)
    price = models.CharField(max_length=45)

class User(models.Model):
    userName = models.CharField(max_length=50)
    userSurname = models.CharField(max_length=50)
    userAge = models.DateField()

class Sales(models.Model):
    user = models.ForeignKey(User)
    product = models.ForeignKey(Product)
    saleType = models.CharField(max_length=50)
    saleDate = models.CharField(max_length=50)