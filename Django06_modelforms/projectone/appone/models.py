from django.db import models

# Create your models here.
class Userprofile(models.Model):

    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    coarsename= models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    joindate=models.DateField()
    