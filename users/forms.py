# users/forms.py

from django.forms import ModelForm, PasswordInput, ValidationError, CharField
from users.models import Student

class RegisterForm(ModelForm):
    confirm_password = CharField(widget=PasswordInput())
    class Meta:
        model = Student
        fields = ["username", "email", "password", "grade"]
        widgets = {
            'password': PasswordInput()
        }
    #extra validation
    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        username = cleaned_data.get("username")
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        #makes sure passwords match
        if password != confirm_password:
            raise ValidationError("Passwords do not match")
        #makes sure password is not the same as email/username
        if password == username or password == email:
            raise ValidationError("Password cannot match username/email")
        #makes sure password has both numberes and letters
        if password.isnumeric() or password.isalpha():
            raise ValidationError("Password must contain both letters and numbers")
        #makes sure username and email are unique
        for item in Student.objects.all():
            if item.username == username or item.email == email:
                raise ValidationError("Username and email must be unique")
        return cleaned_data