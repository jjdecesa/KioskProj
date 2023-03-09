from django.db import models
from datetime import datetime

# Create your models here.
class Content(models.Model):
    filename= models.CharField('filename', max_length=128, null=True, unique=True)
    description= models.CharField(max_length=128, null=True, blank=True)
    date_added= models.DateTimeField(null=True, default=datetime.now)
    active= models.IntegerField(default=0)
    file= models.FileField(upload_to='media/')

    def __str__(self):
        return self.filename

    
class Device(models.Model):
    devicename= models.CharField('devicename', max_length=64, null=True, unique=True)
    description= models.CharField(max_length=128, null=True, blank=True)
    location= models.CharField(max_length=32, null=True, blank=True)
    imagePlaylist = models.ManyToManyField(Content)

    def __str__(self):
        return self.name

