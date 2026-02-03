from django.db import models
# Create your models here.
class BookModel(models.Model):
    bookName = models.CharField(max_length=100) 
    bookDesc = models.CharField(max_length=255) 
    bookAuthor = models.CharField(max_length=50) 
    bookPoster = models.CharField()
    bookPrice = models.IntegerField() 