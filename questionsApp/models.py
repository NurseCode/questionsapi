from django.db import models
from datetime import time, date, datetime

# Create your models here.
class Question(models.Model):
    question = models.CharField(max_length=300)
    metrics = models.CharField(max_length=300)
    tags = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
        
    def __str__(self):
        return self.question
