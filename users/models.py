from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator, MaxLengthValidator, EmailValidator

# Create your models here.
class Student(models.Model):
    username = models.CharField(max_length=150, validators=[MaxLengthValidator(150)])
    email = models.CharField(max_length=150, validators=[MaxLengthValidator(150), EmailValidator()])
    password = models.CharField(max_length=150, validators=[MaxLengthValidator(150), MinLengthValidator(10)])
    grade = models.IntegerField(validators=[MinValueValidator(9), MaxValueValidator(12)])