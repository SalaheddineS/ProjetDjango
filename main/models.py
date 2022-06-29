from django.db import models
from PIL import Image 
from django import forms
# Create your models here.

class Media(models.Model):
    class Meta:
        verbose_name_plural="Media"
    
    timestamp= models.DateTimeField()
    image= models.ImageField(upload_to="media_image")
    url=models.URLField()

from django.contrib.auth.models import User
# Create your models here.


class Task(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True )
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complete']
