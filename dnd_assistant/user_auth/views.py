from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, logout

class RegisterView(View):
    def get(self, request):
        # render the registration form
        return render(request, 'registration/register.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        # validate the form data
        if not username:
            messages.error(request, 'Username is required')
            return redirect('user_auth:register')
        if not password:
            messages.error(request, 'Password is required')
            return redirect('user_auth:register')
        if password != password2:
            messages.error(request, 'Passwords do not match')
            return redirect('user_auth:register')

        # create the user
        user = User.objects.create_user(username=username, password=password)
        login(request, user)

        # redirect to the home page
        return redirect('user_auth:index')

def index(request):
    if "user" not in request.session:
        request.session["user"] = []
         
    return render(request, "registration/index.html",)


def logout_view(request):
    # log the user out
    logout(request)

    # redirect to the home page
    return redirect('user_auth:index')
