from django import forms
from django.contrib.auth.forms import AuthenticationForm


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(
        required=True,
        label="Email",
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Введите Email",
            }
        ),
    )

    def clean_username(self):
        username = self.cleaned_data.get(
            "username"
        ).lower()
        return username
