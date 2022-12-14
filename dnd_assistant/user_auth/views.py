from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import logout

class RegisterView(View):
    def get(self, request):
        # render the registration form
        return render(request, 'registration/register.html')

    def post(self, request):
        # get the form data
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

        # log the user in
        login(request, user)

        # redirect to the home page
        return redirect('user_auth:index')

def my_view(request):
        
    # get the current logged-in user
    current_user = request.user

    # get the username of the current logged-in user
    username = current_user.username

    # get the favorite D&D class of the current logged-in user (assuming you added this field to the User model)
    # favorite_dnd_class = current_user.favorite_dnd_class

def index(request):
    if "user" not in request.session:
        request.session["user"] = []
         
    return render(request, "registration/index.html",)



def logout_view(request):
    # log the user out
    logout(request)

    # redirect to the home page
    return redirect('user_auth:index')
