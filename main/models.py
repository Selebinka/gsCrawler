
import json
from django.db import models
from django.utils import timezone
 

class GoogleResultModel(models.Model):
    keywords = models.CharField(max_length=50)
    title = models.CharField(max_length=255)
    link = models.URLField (max_length=255)
    
    
    def __str__(self):
        return self.title


