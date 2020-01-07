from django.contrib.auth.forms import (
    AuthenticationForm,
    UsernameField,
    PasswordChangeForm,
    PasswordResetForm,
    SetPasswordForm,
)
from django.forms import TextInput, CharField, PasswordInput, EmailField, ModelForm, EmailInput, ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import password_validation
from django.contrib.auth.models import User


class AccountLoginForm(AuthenticationForm):
    username = UsernameField(widget=TextInput(attrs={'autofocus': True, 'class': 'form-control'}))
    password = CharField(
        label=_('Password'),
        strip=False,
        widget=PasswordInput(attrs={'class': 'form-control'}),
    )


class AccountRegisterForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'username': TextInput(attrs={'class': 'form-control'}),
            'email': EmailInput(attrs={'class': 'form-control'}),
            'password': PasswordInput(attrs={'class': 'custom-select'}),
        }

    password = CharField(
        label='Password',
        widget=PasswordInput(attrs={'class': 'form-control'}),
        strip=False,
        required=True,
    )
    confirm_password = CharField(
        label='Confirm Password',
        widget=PasswordInput(attrs={'class': 'form-control'}),
        strip=False,
        required=True,
    )

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])

        if commit:
            user.save()

        return user

    def clean(self):
        cleaned_data = super(AccountRegisterForm, self).clean()
        password = cleaned_data['password']
        confirm_password = cleaned_data["confirm_password"]

        if password != confirm_password:
            raise ValidationError(
                "Password and confirm password do not match!"
            )


class AccountUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        widgets = {
            'username': TextInput(attrs={'class': 'form-control'}),
            'email': EmailInput(attrs={'class': 'form-control'}),
            'first_name': TextInput(attrs={'class': 'form-control'}),
            'last_name': TextInput(attrs={'class': 'form-control'}),
        }


class AccountPasswordChangeForm(PasswordChangeForm):
    old_password = CharField(
        label=_('Old password'),
        strip=False,
        widget=PasswordInput(attrs={'autofocus': True, 'class': 'form-control'}),
    )
    new_password1 = CharField(
        label=_('New Password'),
        strip=False,
        widget=PasswordInput(attrs={'class': 'form-control'}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = CharField(
        label=_('New Password Confirmation'),
        strip=False,
        widget=PasswordInput(attrs={'class': 'form-control'}),
    )


class AccountPasswordResetForm(PasswordResetForm):
    email = EmailField(
        label=_("Email"),
        max_length=254,
        widget=TextInput(attrs={'class': 'form-control'})
    )


class AccountPasswordResetConfirmForm(SetPasswordForm):
    new_password1 = CharField(
        label=_("New password"),
        widget=PasswordInput(attrs={'class': 'form-control'}),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = CharField(
        label=_("New password confirmation"),
        strip=False,
        widget=PasswordInput(attrs={'class': 'form-control'}),
    )
