from django.db import models

# Create your models here.
class Category(models.Model):
    Name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.Name

class Link(models.Model):
    header = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    category = models.ForeignKey(Category)
    
    
    def __str__(self):
        return self.link