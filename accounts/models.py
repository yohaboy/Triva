from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractUser

class CustomManager(BaseUserManager):

    def create_user(self,username,phone_number,password = None , **kwargs):
        if not phone_number:
            raise ValueError("please enter your phone number")
        
        kwargs.setdefault("is_active",True)
        user = self.model(username = username ,phone_number = phone_number ,**kwargs)
        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_superuser(self, username,phone_number,password=None,**kwargs):
        kwargs.setdefault("is_staff",True)
        kwargs.setdefault("is_superuser",True)

        return self.create_user(username,phone_number,password=password ,**kwargs)
    
class CustomUser(AbstractUser):
    username = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50 ,unique=True)
    profile = models.FileField(upload_to="profiles/", blank=True, null=True ,default='profiles/image.png')
    balance = models.DecimalField(decimal_places=2 ,max_digits=10 ,default=0 ,null=True ,blank=True)
    weekly_rank = models.PositiveIntegerField(default=0,null=True, blank=True)
    monthly_rank = models.PositiveIntegerField(default=0,null=True, blank=True)
    total_point = models.PositiveIntegerField(default=0,null=True, blank=True)

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = ["username"]

    objects = CustomManager()

    def __str__(self):
        return f"user: {self.username}"
