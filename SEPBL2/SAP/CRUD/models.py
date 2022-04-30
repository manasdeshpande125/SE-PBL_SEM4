from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.conf import settings
import os
from django.core.exceptions import ValidationError


class Achievements(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    title= models.CharField(max_length=200)
    description=models.CharField(null=True,blank=True,max_length=200)
    support=models.CharField(max_length=200)

    created=models.DateTimeField(auto_now_add=True)
    certificate=models.FileField(blank=False) 

    def __str__(self):
        return self.title


class profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    roll=models.CharField(max_length=200,null=True)
    year=models.CharField(max_length=200,null=True)
    div=models.CharField(max_length=200,null=True)
    dept=models.CharField(max_length=200,null=True)
    #fname=models.CharField(max_length=200,null=True)

    def __str__(self):
        return f'{self.user}'
