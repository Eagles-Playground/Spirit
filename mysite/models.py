#!/usr/bin/env python3
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserProfileManager(BaseUserManager):
    def create_user(
          self, username, email, first_name, last_name, grade, password=None,
          commit=True):
      user = self.model(
          username=username,
          email=self.normalize_email(email),
          first_name=first_name,
          last_name=last_name,
          grade = grade,
      )

      user.set_password(password)
      if commit:
          user.save(using=self._db)
      return user

    def create_superuser(self, username, email, first_name, last_name, password, grade):
        user = self.create_user(
            username = username,
            email = self.normalize_email(email),
            password=password,
            first_name=first_name,
            last_name=last_name,
            grade=grade,
            commit=False,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class UserProfile(AbstractBaseUser):
    username = models.CharField(max_length=100, default='', unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100, default='')
    last_name = models.CharField(max_length=100, default='')
    grade = models.IntegerField(validators=[MinValueValidator(9, message="Enter a Valid Grade"), MaxValueValidator(12, message="Enter a Valid Grade")])
    score1 = models.IntegerField(default=0, blank=True)
    score2 = models.IntegerField(default=0, blank=True)
    score3 = models.IntegerField(default=0, blank=True)

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','first_name', 'last_name', 'grade']

    objects = UserProfileManager()
 
    def __str__(self):
        return self.user.username

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

  