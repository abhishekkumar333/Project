from django.db import models
from djgeojson.fields import PolygonField
# Create your models here.

class provider(models.Model):
	  Service_Areas=PolygonField(default=[])
 	  name=models.CharField(max_length=100, blank=True, default='')
 	  email=models.CharField(max_length=30,blank=True,default='')
   	  phone=models.CharField(max_length=15,blank=True,default='')
 	  Language=models.CharField(max_length=20,blank=True,default='')
 	  Currency=models.CharField(max_length=20,blank=True,default='')
