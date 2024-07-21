from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator

# Create your views here.
class userprofile(models.Model):

    username=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    contact=models.IntegerField(validators=[MaxValueValidator(9999999999),MinValueValidator(1000000000)])
    salary=models.DecimalField(max_digits=12,decimal_places=2,default=0.0)


