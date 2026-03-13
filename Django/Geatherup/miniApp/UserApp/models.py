from django.db import models

# Create your models here.
class User (models.Model):
    fullName = models.CharField(max_length = 100)
    avatar = models.CharField(max_length=400)
    email = models.EmailField()
    bio = models.CharField(max_length=400)
    password = models.CharField(max_length =  100)
