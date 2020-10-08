from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator,
    MinLengthValidator, MaxLengthValidator, EmailValidator

# Create your models here.
class Student(models.Model):
    username = models.CharField(max_length=150,
        validators=[MaxLengthValidator(150, message="Username is too long")])
    email = models.CharField(max_length=150,
        validators=[MaxLengthValidator(150, message="Email is too long"), EmailValidator()])
    password = models.CharField(max_length=150,
        validators=[MaxLengthValidator(150, message="Password is too long"),
        MinLengthValidator(10, message="Password must be 10 characters or longer")])
    grade = models.IntegerField(validators=[MinValueValidator(9, message="Enter a Valid Grade"),
        MaxValueValidator(12, message="Enter a Valid Grade")])