from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class AccountManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, nickname, email, password, *args,**kwargs):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            nickname=nickname,
            email=email,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        max_length=255,
        unique=True,
    )
    nickname = models.CharField(
        max_length=20,
        null=False,
        unique=True
    )
    
    objects = AccountManager()
    
    USERNAME_FIELD = 'nickname'
    REQUIRED_FIELDS = ['email']