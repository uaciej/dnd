from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.views import LoginView

class RegisterView(View):
    def get(self, request):
        # render the registration form
        return render(request, 'user_auth/register.html')

    def post(self, request):
        # get the form data
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        # validate the form data
        if not username:
            messages.error(request, 'Username is required')
            return redirect('register')
        if not password:
            messages.error(request, 'Password is required')
            return redirect('register')
        if password != password2:
            messages.error(request, 'Passwords do not match')
            return redirect('register')

        # create the user
        user = User.objects.create_user(username=username, password=password)

        # log the user in
        login(request, user)

        # redirect to the home page
        return redirect('home')
