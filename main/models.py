
import json
from django.db import models
from django.utils import timezone
 
class GoogleResult(models.Model):
    title = models.CharField(max_length=255)
    link = models.URLField (max_length=255)
    
 
    def __str__(self):
        return self.title