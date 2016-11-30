from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=120)
