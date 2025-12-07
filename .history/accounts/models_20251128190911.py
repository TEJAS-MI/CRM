from django.db import models

# Create your models here.

class Customer(models.model):
    nme=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    
