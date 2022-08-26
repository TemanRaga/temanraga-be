import email
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from rest_framework_simplejwt.tokens import RefreshToken

# Create your models here.
AUTH_PROVIDERS = {'google': 'google', 'email': 'email'}

class UserManager(BaseUserManager):

    def create_user(self, name, email, is_completed, password=None, **kwargs):
        if email is None:
            raise TypeError('Users should have a Email')

        if is_completed == None:
            is_completed = 1
            
        user = self.model(name = name, email=self.normalize_email(email), is_completed=is_completed, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None):
        if password is None:
            raise TypeError('Password should not be none')

        user = self.create_user(name='', email=email, is_completed=1)
        user.set_password(password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOICES = [(0, 'Male'), (1, 'Female')]

    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    is_completed = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    address = models.TextField(blank=True, null=True)
    gender = models.IntegerField(choices=ROLE_CHOICES, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    auth_provider = models.CharField(max_length=255, blank=False, null=False, default=AUTH_PROVIDERS.get('email'))

    USERNAME_FIELD = 'email'

    objects = UserManager()

    def __str__(self):
        return self.email

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        access = refresh.access_token
        access["email"] = self.email
        access["name"] = self.name
        access["gender"] = self.gender
        access["address"] = self.address
        access["is_completed"] = self.is_completed
        return {
            'refresh': str(refresh),
            'access': str(access)
        }