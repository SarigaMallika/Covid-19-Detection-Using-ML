from django.db import models

# Create your models here.
class user_details(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    place = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class medical_details(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    place = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class symp(models.Model):
    age = models.CharField(max_length=100,default="SOME STRING")
    fever = models.CharField(max_length=100,default="SOME STRING")
    fatigue = models.CharField(max_length=100,default="SOME STRING")
    dry_cough = models.CharField(max_length=100,default="SOME STRING")
    loss_of_appetite = models.CharField(max_length=100,default="SOME STRING")
    body_aches = models.CharField(max_length=100,default="SOME STRING")
    shortness_of_breath = models.CharField(max_length=100,default="SOME STRING")
    mucus = models.CharField(max_length=100,default="SOME STRING")
    sore_throat = models.CharField(max_length=100,default="SOME STRING")
    headache = models.CharField(max_length=100,default="SOME STRING")
    chills = models.CharField(max_length=100,default="SOME STRING")
    loss_of_smell = models.CharField(max_length=100,default="SOME STRING")
    stuffy_nose = models.CharField(max_length=100,default="SOME STRING")
    vomiting = models.CharField(max_length=100,default="SOME STRING")
    diarrhea = models.CharField(max_length=100,default="SOME STRING")
    trouble_breathing = models.CharField(max_length=100,default="SOME STRING")
    constant_pain = models.CharField(max_length=100,default="SOME STRING")
    bluish_lips = models.CharField(max_length=100,default="SOME STRING")
    sudden_confusion = models.CharField(max_length=100,default="SOME STRING")
    u_id = models.CharField(max_length=100,default="SOME STRING")
    result = models.CharField(max_length=100,default="SOME STRING")

class message(models.Model):
    u_id = models.CharField(max_length=100, default="SOME STRING")
    message = models.CharField(max_length=1000, default="SOME STRING")

class admin(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)