from __future__ import unicode_literals


# Create your models here.
from collections import defaultdict

from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    has_apt = models.BooleanField(default=False)
    img = models.ImageField(default='images/img.JPG')

class Apartments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    apat_id = models.AutoField(primary_key=True)
    address = models.CharField(max_length=255)
    rooms = models.IntegerField()
    cost = models.IntegerField()
    roommates = models.IntegerField()
    vacancy = models.IntegerField()
    laundry = models.BooleanField()
    internet = models.BooleanField()


class Apartment_images(models.Model):
    apartment = models.ForeignKey(Apartments,on_delete=models.CASCADE)
    img_id = models.AutoField(primary_key=True)
    desc = models.CharField(max_length=255)


