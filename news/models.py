from django.db import models
#from ecc.tinymce import models as tinymce_models
from django.contrib.auth.models import User

PUBLISH_CHOICES = (
        ('Y', 'Yes'),
        ('N', 'No'),
    )

class Entry(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField()
    title = models.CharField(max_length=200)
    #body = tinymce_models.HTMLField()
    #extended = tinymce_models.HTMLField()
    body = models.CharField(max_length=999999)
    extended = models.CharField(max_length=999999)
    author = models.ForeignKey(User)
    publish = models.CharField(max_length=1, choices=PUBLISH_CHOICES,default='Y')

    def get_absolute_url(self):
        return "/newsitem/%i/" % self.id

    def __str__(self):
        return '%s, (%s) : %s' % (self.create_date,self.author,self.title)

