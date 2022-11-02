from django.db import models

# Create your models here.
class EMP_DETAILS(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    salary=models.FloatField(null=True)
    address=models.CharField(max_length=100,null=True)
    email=models.CharField(max_length=20)
    password=models.CharField(max_length=15)
    is_deleted=models.CharField(max_length=2,default='no')
