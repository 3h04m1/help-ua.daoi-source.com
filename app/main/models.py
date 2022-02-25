from pyexpat import model
from django.db import models

class help(models.Model):
    help_type = models.CharField(max_length=20)
    nume = models.CharField(max_length=255)
    tel = models.CharField(max_length=15)
    details = models.TextField(max_length=1000)
    # pub_date = model.

# Create your models here.
