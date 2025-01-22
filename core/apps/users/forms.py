from django import forms
from django.contrib.auth.forms import AuthenticationForm


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Введите почту"}),
    )

    password = forms.CharField(
        required=False,
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "current-password",
                "class": "form-control",
                "placeholder": "Введите пароль",
            }
        ),
    )

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if username == "":
            return self.add_error("username", "Почта не может быть пустой")
        elif "@" not in username or "." not in username:
            return self.add_error("username", "Почта введена некоректно")
        return username

    def clean_password(self):
        password = self.cleaned_data.get("password")
        if password == "":
            return self.add_error("password", "Пароль не может быть пустым")
        return password

    def is_valid(self):
        errors = self.errors.as_data()
        for field in self.fields:
            if field not in errors:
                self.fields[field].widget.attrs.update({"class": "form-control is-valid"})
            else:
                self.fields[field].widget.attrs.update({"class": "form-control is-invalid"})
        return super().is_valid()
