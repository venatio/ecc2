from django.db import models

# Create your models here.
class Contact(models.Model):
    display_order = models.IntegerField()
    role = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    telephone = models.CharField(max_length=50,null=True, blank=True)
    mobile = models.CharField(max_length=50,null=True, blank=True)
    email = models.CharField(max_length=50,null=True, blank=True)
    
    
    def __str__(self):
        return '%s %s: %s' % (self.display_order,self.role,self.name)