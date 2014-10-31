from django.db import models

# Create your models here.

class Piado(models.Model):
  text = models.CharField(max_length=140)

