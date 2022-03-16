from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class CustomAccountManager(BaseUserManager):

    def create_user(self, email, username, firstname, password, **other_fields):
        if not email:
            raise ValueError(_('You must provide an email address'))
        email = self.normalize_email(email)
        user = self.model(
            email=email, 
            username=username, 
            firstname=firstname,
            **other_fields
            )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, username, firstname, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError("Superuser must be assign to is_staff=True.")
        if other_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must be assign to is_superuser=True.")
        return self.create_user(email, username, firstname, password, **other_fields)

    
        

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(max_length = 150, unique=True)
    firstname = models.CharField(max_length = 150)
    start_date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    about = models.TextField(_('about'), blank=True)
    
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','firstname']

    objects=CustomAccountManager()

    def __str__(self):
        return self.username
        
    
