from django.db import models

# Create your models here.
class Question(models.Model):
    question = models.CharField(max_length=300)
    metrics = models.CharField(max_length=300)
    tags = models.CharField(max_length=250)
    
    def __str__(self):
        return self.question
    
    