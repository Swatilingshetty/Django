from django.db import models

# Create your models here.
class product(models.Model):
    Productbrandname=models.CharField(max_length=100)
    Productbrandmodel=models.CharField(max_length=100)
    Productbrandcost=models.FloatField()