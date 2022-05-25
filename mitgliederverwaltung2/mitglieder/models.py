from django.db import models

# Create your models here.

class Mitglieder(models.Model):
  vname = models.CharField(max_length=255)
  nname = models.CharField(max_length=255)
  email = models.EmailField(max_length=255)
  mitgliedsnr = models.IntegerField(primary_key=True)