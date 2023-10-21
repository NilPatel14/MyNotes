from django.db import models

class MyNote(models.Model):
    title = models.CharField(max_length=200,default="null")
    content = models.CharField(max_length=2000,default="null")
    
# Create your models here.
