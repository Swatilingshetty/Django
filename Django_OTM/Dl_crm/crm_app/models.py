from django.db import models
from django.utils import timezone

# Create your models here.
class createnewlead(models.Model):

    LEAD_STATUS_CHOICES=[
        ('None','None'),
        ('NotContacted','NotContacted'),
       ( 'Attempted','Attempted'),
        ('WarmLead','WarmLead'),
        ('Opportunity','Opportunity'),
        ('AttendedDemo','AttendedDemo'),
        ('Visited','Visited'),
        ('Registered','Registered'),
       ( 'Coldlead','Coldlead'),
    ]

    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255)
    cc=models.BigIntegerField()
    contact_no=models.BigIntegerField()
    email=models.EmailField(max_length=255)
    fee_coated=models.DecimalField(max_digits=10,decimal_places=2)
    description=models.TextField()
    date=models.DateField(default=timezone.now)

    lead_status=models.CharField(
        max_length=12,
        choices=LEAD_STATUS_CHOICES,
        default='None',
    )