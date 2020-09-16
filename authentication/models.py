# from django.db import models
# from django.contrib.auth.models import (
#     AbstractBaseUser, BaseUserManager, PermissionsMixin
# )
# from rest_framework_jwt.settings import api_settings
# # Our JWT payload
# jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
# jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
# class UserManager(BaseUserManager):
#     """
#     Django requires that custom users define their own Manager class. By
#     inheriting from `BaseUserManager`, we get a lot of the same code used by
#     Django to create a `User`.
#     All we have to do is override the `create_user` function which we will use
#     to create `User` objects.
#     """
#     def create_user(self, username, password=None, first_name=None,
#                     last_name=None):
#         """
#         Create and return a `User` with an email, username, first_name, last_name
#         and password.
#         """
#         if username is None:
#             raise TypeError("Users must have a username")
#         # if email is None:
#         #      raise TypeError("Users must have an email address")
#         user = self.model(
#             username=username,
#             # email=self.normalize_email(email),
#             first_name=first_name,
#             last_name=last_name,
#             is_staff=False,
#         )
#         user.set_password(password)
#         user.save()
#         return user
#     def create_superuser(self, username, password):
#         """
#         Create and return a `User` with superuser (admin) permissions.
#         """
#         if password is None:
#             raise TypeError("Superusers must have a password")
#         user = self.create_user(username, password)
#         user.is_superuser = True
#         user.is_staff = True
#         user.save()
#         return user
# class User(AbstractBaseUser, PermissionsMixin):
#     """
#     Class to represent user model
#     """
#     username = models.CharField(db_index=True, max_length=255, unique=True)
#     #email = models.CharField(db_index=True,max_length=255)
#     first_name = models.CharField(max_length=255, null=True, blank=True)
#     last_name = models.CharField(max_length=255, null=True, blank=True)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     USERNAME_FIELD = 'username'
#     # REQUIRED_FIELDS = ['email']
#     # *** REQUIRED_FIELDS = ['email', 'first_name', 'last_name'] ***
#     # Tells Django that the UserManager class defined above should manage
#     # objects of this type.
#     objects = UserManager()
#     def __str__(self):
#         """
#         Returns a string representation of this `User`.
#         This string is used when a `User` is printed in the console.
#         """
#         return self.username
#     @property
#     def token(self):
#         """
#         Allows us to get a user's token by calling `user.token` instead of
#         `user.generate_jwt_token().
#         The `@property` decorator above makes this possible. `token` is called
#         a "dynamic property".
#         """
#         return self._generate_jwt_token()
#     def _generate_jwt_token(self):
#         """
#         Generates a JSON Web Token that stores this user's instance and has an expiry
#         date set to 60 days into the future.
#         """
#         payload = jwt_payload_handler(self)
#         token = jwt_encode_handler(payload)
#         return token

from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)
# allows us to access the JWT settings
from rest_framework_jwt.settings import api_settings
# sets up the JWT payload (data sent with token)
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
"""
Default Django Authorization User Model Documentation:
https://docs.djangoproject.com/en/3.0/ref/contrib/auth/#django.contrib.auth.models.User.is_staff
"""
# Create your models here.
# allows us to create a regular user or a superuser
class UserManager(BaseUserManager):
    def create_user(self, username, password=None, first_name=None, last_name=None):
        # the above args indicate that the default values for first/last name and password are None
        # indicates they are not required.
        if username is None:
            raise TypeError("Users must have a username.")
        # if email is None:
        #     raise TypeError("Users must have an email address.")
        # create the user object
        # self.normalize_email is inbuilt method to django that strips white space and lowercases
        user = self.model(
            username= username,
            # email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            is_staff=False
        )
        user.set_password(password)
        user.save()
        return user
    # this is creating a superuser administrator
    def create_superuser(self, username, password):
        if password is None:
            raise TypeError("Superusers must have a password.")
        user = self.create_user(username, password)
        user.is_superuser=True
        user.is_staff=True
        user.save()
        return user
# This class is for people who are using the site, logging in etc. Not for superusers
class User(AbstractBaseUser, PermissionsMixin):
    # db_index gives the user a unique index in the database
    # unique ensures the username doesn't already exist in database
    # these are all built in methods to the AbstractBaseUser
    # email = models.EmailField(db_index=True, unique=True)
    username = models.CharField(db_index=True, max_length=255, unique=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    USERNAME_FIELD = 'username'
    # REQUIRED_FIELDS = ['email'] # this is an array, could have more required fields
    objects = UserManager()
    def __str__(self):
        return self.username
    @property
    def token(self):
        return self._generate_jwt_token()
    """
    Generates a JSON Web Token that stores this(self) object /user instance
    and has an expiration date set to 60 days from creation of token
    """
    # a single underscore before a method name is a 'PROTECTED' method.
    def _generate_jwt_token(self):
        payload = jwt_payload_handler(self)
        token = jwt_encode_handler(payload)
        return token