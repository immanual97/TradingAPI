from datetime import date
from pyexpat import model
from django.db import models

# Create your models here.
class Trade(models.Model):
    date=models.CharField(max_length=25)
    open=models.CharField(max_length=25)
    high=models.CharField(max_length=25)
    low=models.CharField(max_length=25)
    close=models.CharField(max_length=25)
    adjclose=models.CharField(max_length=25)
    volume=models.CharField(max_length=25)