from django.db import models
from django.utils import timezone
import uuid

class Hirer(models.Model):
    '''Data template for hiring parties'''
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    email_address = models.EmailField(max_length=255, unique=True)
    hashed_password = models.CharField(max_length=128, default=' ')
    phone_no = models.IntegerField(null=True)
    joined = models.DateField(default=timezone.now)

class job(models.Model):
    '''Model for job(s) created by a hirer'''
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=255, null=True)
    description = models.TextField()
    pay = models.IntegerField()
    posted_on = models.DateField(default=timezone.now)
    hirer_id = models.CharField(max_length=255, null=True) # hirer.id to be passed on job creation