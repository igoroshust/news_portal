from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from allauth.account.forms import SignupForm
from django.core.mail import send_mail # отправка писем


class SignUpForm(UserCreationForm):
    """Регистрация пользователей"""
    username = forms.CharField(label="Логин")
    first_name = forms.CharField(label="Имя")
    last_name = forms.CharField(label="Фамилия")
    email = forms.EmailField(label="Почта")
    password1 = forms.CharField(label="Пароль")
    password2 = forms.CharField(label="Подтверждение пароля")

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        )

class CustomSignupForm(SignupForm):
    def save(self, request):
        user = super().save(request)
        authors_users = Group.objects.get(name="authors")
        user.groups.add(authors_users)
        return user