from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from spirit.models import UserProfile
from django.forms import ModelForm, ValidationError


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = UserProfile
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'grade',
            'password1',
            'password2'
        )

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        username = cleaned_data.get("username")
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password != confirm_password:
            raise ValidationError("Passwords do not match")
        if password == username or password == email:
            raise ValidationError("Password cannot match username/email")
        return cleaned_data

class EditProfileForm(UserChangeForm):
    template_name='/something/else'

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'password'
        )
      
class updateScore2(forms.Form):
  score = forms.IntegerField()

  def clean(self):
    data = self.cleaned_data['score']
    