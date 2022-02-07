from django.db import models

# Create your models here.
class Expense(models.Model):
    amount = models.FloatField()
    merchant = models.CharField(max_length=500)
    description = models.CharField(max_length=500, blank=True, null=True)
    category = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
