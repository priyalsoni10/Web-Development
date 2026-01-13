from django.db import models

class Task(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)  # Task description
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.name


# Create your models here.
