# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ..login_and_registration.models import Users

from django.db import models

# Create your models here.

class BuyGroup(models.Model):
    name=models.CharField(max_length=255)
    admin=models.ForeignKey(Users, related_name="group")
    ta=models.ForeignKey(Users, related_name="ta_group")
    user=models.ForeignKey(Users, related_name="user_group")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Items(models.Model):
    item_name= models.CharField(max_length=255)
    voters = models.ManyToManyField(Users, related_name="votes")
    picture = models.CharField() # to be changed and figured out
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Inventory(models.Model):
    count = models.IntegerField()
    item = models.ForeignKey(Items, related_name="stock")
    unit = models.CharField(max_length=255)
    expiration = models.DateField()
    amount_used = models.IntegerField()
    max_inventory = models.IntegerField()
    min_inventory = models.IntegerField()



