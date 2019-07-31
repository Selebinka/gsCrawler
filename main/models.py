
import json
from django.db import models
from django.utils import timezone
 

class GoogleResultModel(models.Model):
    positionID = models.CharField(max_length=200)
    keywords = models.CharField(max_length=50)
    title = models.CharField(max_length=255)
    link = models.URLField (max_length=255)
    date = models.DateField(auto_now_add=True)
    
    
    def __str__(self):
        return self.title


