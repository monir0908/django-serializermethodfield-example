from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, 
    PermissionsMixin,
    BaseUserManager,
    )
class UserManager(BaseUserManager):
    def _create_user(self, email, mobile, first_name, last_name, password, **extra_fields):
        if not email:
            raise ValueError("email is not provided")
        if not password:
            raise ValueError("password is not proided")

        user = self.model(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            mobile = mobile,
            **extra_fields
        )

        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_user(self, email, mobile, first_name, last_name, password, **extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('is_superuser',False)
        return self._create_user(email, mobile, first_name, last_name, password, **extra_fields)

    def create_superuser(self, email, mobile, first_name, last_name, password, **extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('is_superuser',True)
        return self._create_user(email, mobile, first_name, last_name, password, **extra_fields)



# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(db_index=True, unique=True, max_length=254)
    mobile = models.CharField(max_length=50)
    first_name = models.CharField(max_length=254)
    last_name = models.CharField(max_length=254)
    address = models.TextField()

    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = True)
    is_superuser = models.BooleanField(default = False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['mobile', 'first_name', 'last_name']

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    