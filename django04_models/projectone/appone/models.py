from django.db import models


# Create your views here.
class userprofile(models.Model):

    username=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    contact=models.IntegerField()


# def __str__(self):
#         return self.username