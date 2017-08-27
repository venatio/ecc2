from django.db import models
#from ecc.tinymce import models as tinymce_models

# Create your models here.
class Game(models.Model):
    year = models.PositiveIntegerField(null=True, blank=False)
    event = models.CharField(null=True,max_length=30)
    white = models.CharField(max_length=30)
    black = models.CharField(max_length=30)
    result = models.CharField(max_length=30)
    game_description = models.TextField(null=True, blank=True)
    game_pgn = models.TextField(null=True, blank=True)
    
    
    def __str__(self):
        return "%s %s: %s v %s (%s) " %(self.year,self.event,self.white,self.black,self.result)



