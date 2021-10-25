from django.db import models

# Create your models here.

class stocks(models.Model):
    symbol = models.CharField(max_length=50, blank = True, null = True)
    expiry = models.DateField()