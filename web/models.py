from django.db import models

# Create your models here.
class Movie(models.Model):
    moviename=models.CharField(max_length=20)

class Phoneprice(models.Model):
    id=models.CharField(max_length=100,primary_key=True)
    maxprice=models.IntegerField()
    opprice=models.IntegerField()
    pprice=models.IntegerField()