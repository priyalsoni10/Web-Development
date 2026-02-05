from django.db import models
# from AuthorApp.models import AuthorModel

# Create your models here.
# class AuthorModel(models.Model):
#     name = models.CharField(max_length=100)
#     age = models.IntegerField()

class AuthorModel(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name
