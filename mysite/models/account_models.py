from django.db import models

from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self,email,password=None):
        if not email:
            raise ValueError("Users must have an email address")
        user=self.model(email=self.normalize_email(email),)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,email,password=None):
        user = self.create_user(email,password)
        user.is_admin=True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    email=models.EmailField(
        max_length=255,
        unique=True,#emailは他の人と被って位はいけない
    )

    is_active=models.BooleanField(default=True) #有効した段階で有効になったことを示す。
    is_admin=models.BooleanField(default=False) #管理画面に入れるかどうか(アカウント作成してadminに入れたらいけないのでFalse)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email ## emailを返す
    
    def has_perm(self,perm,obj=None):
        "Does the user have a specific permission?"
        return True
    
    def has_module_perms(self,app_label):
        "Does the user have permissions to view the app app_label ?"
        return True
    
    @property
    def is_staff(self):
        return self.is_admin


# OneToOne Fieldを同時に作成#
from django.db.models.signals import post_save 
from django.dispatch import receiver

@receiver(post_save, sender=User)#通史のような処理
def create_onetoone(sender,**kwargs):##キーワード引数->可変長の引数を受け入れる
    if kwargs["created"]:
        from mysite.models.profile_models import Profile
        
        Profile.objects.create(user=kwargs["instance"])