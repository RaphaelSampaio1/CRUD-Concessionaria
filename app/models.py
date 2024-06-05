from django.db import models

# Create your models here.
class carros(models.Model):
    modelo= models.CharField(max_length=150)
    marca= models.CharField(max_length=80)
    ano= models.IntegerField()