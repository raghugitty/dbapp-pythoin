from django.db import models
#from django.contrib.auth import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import User
#Create your models here.
class pollvoters(models.Model):  
    first_name = models.CharField(max_length=200)  
    last_name = models.CharField(max_length=200)  
    address = models.CharField(max_length=200, null =True)  
    restaurant = models.CharField(max_length=200, null = True)  
    Location = models.CharField(max_length=100, null = True)

# class User(models.AbstractBaseUser):
#     user_name = models.CharField(max_length=100)
#     phone_number = models.CharField(max_length=11)
#     role      = models.CharField(max_length=100, null =True)
#     objects = managers.UserManager()
#     @classmethod
#     def create_user(cls, email):
#         if email and not User.objects.filter(email=email).exists():
#             role, _ = role_master.objects.get_or_create(name='User')
#             User.objects.create_user(email=email, roles=role)


# class person(models.Model):
#     user=models.OneToOneField(User, on_delete=models.CASCADE, related_name= 'person')
#     age=models.PositiveSmallIntegerField()
#     bio=models.CharField(max_length=256)