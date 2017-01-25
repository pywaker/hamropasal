from django.db import models
from django.db.models import Model


# Create your models here.
class Category(Model):
    name = models.CharField(max_length=32)
    description = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    category = models.ForeignKey('self', blank=True, null=True, 
                                 verbose_name='Parent', related_name='children')
    
    #def __init__(self, *args, **kwargs):
        ##self.name = name
        ##self.description = description
        #super().__init__(*args, **kwargs)
    
    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=32)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, blank=True, null=True)

    def __str__(self):
        return self.name
    
    def __repr__(self):
        return self.name
    