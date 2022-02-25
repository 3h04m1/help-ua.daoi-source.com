# from pyexpat import model
from django.db import models

class Help(models.Model):
    help_type = models.CharField(max_length=20)
    name = models.CharField(max_length=255)
    tel = models.CharField(max_length=15)
    details = models.TextField(max_length=1000)
    pub_date = models.TimeField(auto_now_add=True)
    mod_date = models.TimeField(auto_now=True)
    link = models.URLField(max_length=1000, blank=True)
    address = models.CharField(max_length=1000, default="Moldova")
    

class NeedHelp(models.Model):
    help_type = models.CharField(max_length=20)
    name = models.CharField(max_length=255)
    tel = models.CharField(max_length=15)
    details = models.TextField(max_length=1000)
    pub_date = models.TimeField(auto_now_add=True)
    mod_date = models.TimeField(auto_now=True)
    link = models.URLField(max_length=1000, blank=True)
    address = models.CharField(max_length=1000, default="Moldova") 

# Create your models here.
