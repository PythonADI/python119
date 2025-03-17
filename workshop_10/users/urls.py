from django.urls import path
from users.views import LoginView, LogoutView, RegisterUser

app_name = "users"

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", RegisterUser.as_view(), name="register"),
]
