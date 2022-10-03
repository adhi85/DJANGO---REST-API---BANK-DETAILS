from django.db import models

# Create your models here.

class Bank(models.Model):
    ifsc = models.CharField(primary_key=True ,max_length=200)
    bank_id = models.PositiveIntegerField()
    branch = models.CharField(max_length=200)
    address = models.TextField(max_length=500)
    city = models.CharField(max_length=200)
    district = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    bank_name = models.CharField(max_length=200)