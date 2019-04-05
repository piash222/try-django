from django.db import models

# Create your models here.
class Products(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null = True)
    price = models.DecimalField(max_digits=100, decimal_places=2)
    summery = models.TextField(blank = False, null=False)
    featured = models.BooleanField(default=True)
