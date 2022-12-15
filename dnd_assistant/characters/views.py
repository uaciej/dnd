from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Character


@login_required
def create_character(request):
    if request.method == 'POST':
        # Get the form data from the request
        name = request.POST.get('name')
        race = request.POST.get('race')
        character_class = request.POST.get('class')
        abilities = request.POST.get('abilities')
        hit_points = request.POST.get('hit_points')
        strength = request.POST.get('strength')
        dexterity = request.POST.get('dexterity')
        constitution = request.POST.get('constitution')
        intelligence = request.POST.get('intelligence')
        wisdom = request.POST.get('wisdom')
        charisma = request.POST.get('charisma')

        

        # Create a new Character instance and save it to the database
        character = Character.objects.create(
            user=request.user,
            name=name,
            race=race,
            character_class=character_class,
            abilities=abilities,
            hit_points=hit_points,
            strength=strength,
            dexterity=dexterity,
            constitution=constitution,
            intelligence=intelligence,
            wisdom=wisdom,
            charisma=charisma,
        )
        
        character.calculate_modifiers()

        character.save()

        # Redirect the user to the character detail page
        return redirect('display_characters')

    # If the request is not a POST request, display the create character form
    return render(request, 'create_character.html')

@login_required
def display_characters(request):
    # Get all characters associated with the logged-in user
    characters = Character.objects.filter(user=request.user)

    # Render the character list template, passing the characters to the template
    return render(request, 'character_list.html', {'characters': characters})

@login_required
def delete_character(request, character_id):
    # Get the character to delete
    character = get_object_or_404(Character, id=character_id)

    # Check if the logged-in user is the owner of the character
    if character.user != request.user:
        return redirect('display_characters')

    # Delete the character
    character.delete()

    # Redirect to the character list page
    return redirect('display_characters')