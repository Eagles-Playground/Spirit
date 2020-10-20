#from django import forms
from django.contrib import admin
#from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
#from django.contrib.auth.forms import ReadOnlyPasswordHashField
#from .models import User
from spirit.models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'grade')

    def get_queryset(self, request):
        queryset = super(UserProfileAdmin, self).get_queryset(request)
        queryset = queryset.order_by('first_name', 'username')
        return queryset

admin.site.register(UserProfile, UserProfileAdmin)


"""
class AddUserForm(forms.ModelForm):
    password1 = forms.CharField(
        label='Password', widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label='Confirm password', widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'grade', 'score1', 'score2', 'score3')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UpdateUserForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = (
            'email', 'password', 'first_name', 'last_name', 'grade', 'score1', 'score2', 'score3', 'is_active',
            'is_staff'
        )

    def clean_password(self):
# Password can't be changed in the admin
        return self.initial["password"]


class UserAdmin(BaseUserAdmin):
    form = UpdateUserForm
    add_form = AddUserForm

    list_display = ('email', 'first_name', 'last_name', 'grade', 'score1', 'score2', 'score3', 'is_staff')
    list_filter = ('is_staff', )
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'grade''score1', 'score2', 'score3')}),
        ('Permissions', {'fields': ('is_active', 'is_staff')}),
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': (
                    'email', 'first_name', 'last_name', 'grade', 'score1', 'score2', 'score3', 'password1',
                    'password2'
                )
            }
        ),
    )
    search_fields = ('email', 'first_name', 'last_name', 'grade', 'score1', 'score2', 'score3')
    ordering = ('email', 'first_name', 'last_name', 'grade', 'score1', 'score2', 'score3')
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
"""