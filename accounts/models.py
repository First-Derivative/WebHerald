from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class AccountManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError("Users require an email address")
        if not username:
            raise ValueError("Users require a username")

        user = self.model(
            email = self.normalize_email(email),
            username = username
        )

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password = password
        )

        user.is_admin = True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name="email",max_length=50, unique=True)

    # required fields
    username = models.CharField(max_length=30, unique=True)
    timestamp = models.DateTimeField(verbose_name='Registration timestamp', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='Last login timestamp', auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username',)

    objects = AccountManager()

    def __str__(self):
        return self.username

    #default override for has_perm
    def has_perm(self, perm, obj=None):
        return self.is_admin

    #default override for has_module_perms
    def has_module_perms(self, app_label):
        return self.is_active

    @property
    def is_staff(self):
        return self.is_admin