from django.db import models

# Create your models here.

class Customer(models.model):
    nme=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    date_created=models.DateTimeField(auto_now_add=T)
