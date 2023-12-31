from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings
import datetime

class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, name, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('User must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password) #make sure password is encrypted
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Create and save a new super user with given details"""
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True) #every email in database needs to be unique
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False) #determines if the user is a staff users

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retrieve full name of user"""
        return self.name #defines a function that returns the full name of the users

    def get_short_name(self):
        """Retrieve short name of user"""
        return self.name

    def _str__(self):
        """Return string representation of our user"""
        return self.email



class ProfileFeedItem(models.Model):
    """Profile status update"""
    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return the model as a string"""
        return self.status_text

def get_upload_path(instance, filename):
    # Assuming your model has an 'id' field
    instance_id = instance.id

    # Create a new filename using the instance ID
    new_filename = f"{datetime.datetime.now().time()}_{filename}"

    # Return the full upload path
    return 'Datapoint Images/'+new_filename


class DataPoint(models.Model):
     user_profile = models.ForeignKey(
         settings.AUTH_USER_MODEL,
         on_delete=models.CASCADE
     )
     bullet_group = models.FloatField()
     point_calc = models.FloatField()
     image_saved = models.FileField(default=None, blank=True, null=True, upload_to=get_upload_path)
