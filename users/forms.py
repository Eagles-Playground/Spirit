# users/forms.py
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)
=======
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
    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        username = cleaned_data.get("username")
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password != confirm_password:
            raise ValidationError("Passwords do not match")
        if password == username or password == email:
            raise ValidationError("Password cannot match username/email")
        if password.isnumeric() or password.isalpha():
            raise ValidationError("Password must contain both letters and numbers")
        return cleaned_data
