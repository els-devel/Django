from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import User
from django.conf import settings
import uuid
import subprocess

class UserProfileManager(BaseUserManager):
    """Manager for User Profiles
    can interchange UserManager for Base User Manager"""

    def create_user(self, email, name, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        # this makes sure that the second half of the email address is all lowercase

        user = self.model(email=email, name=name)
        # creates a new user (model object)

        user.set_password(password)
        # by default, django encrypts the password when storing in database
        # doesn't mean you dont have to put additional protection for database
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Create and save a new superuser with given details"""
        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retrieve full name of user"""
        return self.name

    def get_short_name(self):
        """Retrieve short name of user"""
        return self.name

    def __str__(self):
        """Return string representation of our user"""
        return self.email


class DatabaseItem(models.Model):
    """Profile status update"""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    key = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    # user_profile = models.ForeignKey(
    #     settings.AUTH_USER_MODEL,
    #     on_delete=models.CASCADE,
    # )

    def make_entry(self, key, value):
        pk = self.id
        key = key
        value = value
        created_on = self.created_on
        #subprocess.run("psql...INSERT (id,  ))
        return f"made database entry ({pk}, {key}, {value}, {created_on}"

    def get_value(self, key):
        #subprocess.run("psql -U postgres -c SELECT * ON TABLE secrets FOR key ({key});"
        return f"getting the value for {key}..."

    def __str__(self):
        """Return the model as a string"""
        return f"{self.key} item"


#class SecretsManager(models.manager.BaseManager):
class SecretsManager(BaseUserManager):

    def __str__(self):
        return "Secrets Manager Object"
    # def create_secret(self, key, value):
    #     kv = self.model(key=key, value=value)
    #     return kv



class Secrets(models.Model):
    """Profile status update"""

    id = models.UUIDField(primary_key=True, default=str(uuid.uuid4()), editable=False)
    key = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    objects = SecretsManager()

    def get_value(self, key):
        #subprocess.run("psql -U postgres -c SELECT * ON TABLE secrets FOR key ({key});"
        return f"getting the value for {key}..."

    def __str__(self):
        """Return the model as a string"""
        return f"{self.key} item"


