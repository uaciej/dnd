from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

app_name = "user_auth"
urlpatterns = [
    path("", views.index, name="index"),
    path("logout", views.logout_view, name="logout"),
    path("login", LoginView.as_view(), name="login"),
    path("register", views.RegisterView.as_view(), name="register")
]