from django.db import models
from django.contrib.auth import get_user_model

from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
# Create your models here.
import os

def upload_image_to(instance,filename):
    user_id = str(instance.user.id)
    # directory = os.path.join("static","image",user_id)

    # root = os.path.abspath(os.path.dirname(__file__))
    # full_path = os.path.join(root,directory)
    # os.makedirs(full_path,exist_ok=True)
    # return os.path.join(directory,filename)
    return os.path.join("static","image",user_id,filename)

class Profile(models.Model):
    user = models.OneToOneField(get_user_model(),unique=True,on_delete=models.CASCADE,primary_key=True)##この項目のFieldがIDになる
    username = models.CharField(default="annonymous",max_length=30)

    zipcode = models.CharField(default="",max_length=8)

    prefecture= models.CharField(default="",max_length=10)

    city = models.CharField(default="",max_length=100)
    address = models.CharField(default="",max_length=200)
    images = models.ImageField(default="",blank=True,upload_to=upload_image_to)
