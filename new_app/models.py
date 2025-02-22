from django.db import models
class trap(models.Model):
 
 place = models.CharField(max_length=255)
 weather =models.CharField(max_length=255) 
 time = models.DateTimeField()
 # Create your models here.
