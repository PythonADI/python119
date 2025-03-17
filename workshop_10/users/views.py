from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView as DjangoLoginView, LogoutView as DjangoLogoutView
from django.views.generic import CreateView
from users.models import User
from users.forms import UserCreationForm


class LoginView(DjangoLoginView):
    template_name = "users/login.html"
    next_page = "/"
    redirect_authenticated_user = True


class LogoutView(DjangoLogoutView):
    next_page = reverse_lazy("users:login")


class RegisterUser(CreateView):
    template_name = "users/register.html"
    success_url = reverse_lazy("users:login")
    form_class = UserCreationForm
    model = User
