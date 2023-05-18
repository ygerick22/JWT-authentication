from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.contrib.auth.hashers import make_password


class UserManager(BaseUserManager):
    def create_user(self, user_email, password=None, **extra_fields):
        if not user_email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(user_email)
        user = self.model(user_email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, user_email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields['password'] = make_password(password)
        return self.create_user(user_email, **extra_fields)



class User(AbstractBaseUser, PermissionsMixin):
    user_ID = models.BigAutoField(primary_key=True)
    user_email = models.EmailField(unique=True)
    First_Name = models.CharField(max_length=30)
    Last_Name = models.CharField(max_length=30)
    Created_on = models.DateTimeField(auto_now_add=True)
    Updated_On = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'user_email'
    REQUIRED_FIELDS = ['First_Name', 'Last_Name']

    objects = UserManager()

    def __str__(self):
        return self.user_email


class UserToken(models.Model):
    token_id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_in = models.BigIntegerField(default=1800)
    token = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Token ID: {self.token_id}, User: {self.user.user_email}"

