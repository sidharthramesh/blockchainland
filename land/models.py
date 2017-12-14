from django.db import models

# Create your models here.
class Land(models.Model):
    name = models.CharField(max_length=200)
    asset_id = models.CharField(max_length=200)
class CryptoUser(models.Model):
    name = models.CharField(max_length=200)
    public_key = models.CharField(max_length=200)

