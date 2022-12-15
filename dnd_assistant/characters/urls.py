from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import display_characters, create_character, delete_character

appname = "characters"
urlpatterns = [
    # Other URL patterns...
    # Create a new character
    path('create', login_required(create_character), name='create_character'),

    # Display the logged-in user's characters
    path('', login_required(display_characters), name='display_characters'),
    
    # Delete the logged-in user's character
    path('<int:character_id>/delete/', delete_character, name='delete_character'),
]
