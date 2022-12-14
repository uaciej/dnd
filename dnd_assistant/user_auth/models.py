from django.db import models

from django.contrib.auth.models import User

# Create your models here.

# get the current logged-in user
current_user = request.user

# get the username of the current logged-in user
username = current_user.username

# get the favorite D&D class of the current logged-in user (assuming you added this field to the User model)
# favorite_dnd_class = current_user.favorite_dnd_class
