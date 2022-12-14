from django.urls import path
from . import views

app_name = "user_auth"
urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register')
]
