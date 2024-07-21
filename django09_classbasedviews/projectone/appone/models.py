from django.db import models

# Create your models here.
class product(models.Model):
    productbrandname=models.CharField(max_length=100)
    productbrandmodel=models.CharField(max_length=100)
    productbrandcost=models.FloatField()

    def get_absolute_url(self):

        return reverse('detail', kwargs={'pk':self.pk})    #kwargs is used for dictionary,arguments for tuples