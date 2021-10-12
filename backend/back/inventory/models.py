from django.db import models

# Create your models here.
class products(models.Model):

    pro_name=models.CharField(max_length=50)
    pro_provider=models.CharField(max_length=50)
    pro_existences=models.PositiveIntegerField()
    pro_date=models.DateField()
    pro_description=models.CharField(max_length=250)
    pro_category=models.CharField(max_length=50)