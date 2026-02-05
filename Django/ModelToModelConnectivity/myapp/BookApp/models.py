from django.db import models
# from .models import BookModel
# from AuthorApp.models import AuthorModel

# class BookModel(models.Model):
#     title = models.CharField(max_length=100)
#     author = models.ForeignKey(AuthorModel, on_delete=models.CASCADE)
    
# Create your models here.
class BookModel(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(
        'AuthorApp.AuthorModel',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title