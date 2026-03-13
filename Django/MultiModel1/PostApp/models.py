from django.db import models

from UserApp.models import User

# Create your models here.
class PostModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    image = models.CharField(max_length=400)
    uploadedBy = models.ForeignKey(User, on_delete=models.CASCADE)