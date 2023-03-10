from django.db import models
from django.contrib.auth.models import *


# Create your models here.

class User(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=10)
    password=models.CharField(max_length=100,blank=True,null=True)
    is_active=models.BooleanField(default=True)


class Questions(models.Model):
    question =models.CharField(max_length=100)
    option_1=models.CharField(max_length=100)
    option_2=models.CharField(max_length=10)
    option_3=models.CharField(max_length=100,blank=True,null=True)
    option_4=models.CharField(max_length=100)
    correct_ans =models.CharField(max_length=100)
    is_active=models.BooleanField(default=True)
    qno = models.CharField(max_length=100,default=1)

    

class Attemp(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    queattempt = models.ForeignKey(Questions, on_delete=models.CASCADE)
    queno=models.CharField(max_length=100)
    ans=models.CharField(max_length=100)
    marking=models.BooleanField()


class Submission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    submitstatus = models.CharField(max_length=200)
    corr_ans = models.CharField(max_length=100)
    persentage = models.CharField(max_length=100)
    attm= models.CharField(max_length=100)
    totq= models.CharField(max_length=100)
    submission_time = models.DateTimeField(auto_now_add=True)






    

    
