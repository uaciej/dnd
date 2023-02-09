from django.db import models
from django.contrib.auth.models import User

class Character(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    race = models.CharField(max_length=100)
    character_class = models.CharField(max_length=100)
    abilities = models.TextField()
    hit_points = models.IntegerField()
    strength = models.IntegerField()
    dexterity = models.IntegerField()
    constitution = models.IntegerField()
    intelligence = models.IntegerField()
    wisdom = models.IntegerField()
    charisma = models.IntegerField()

    # Modifier fields
    strength_modifier = models.IntegerField(blank=True, null=True)
    dexterity_modifier = models.IntegerField(blank=True, null=True)
    constitution_modifier = models.IntegerField(blank=True, null=True)
    intelligence_modifier = models.IntegerField(blank=True, null=True)
    wisdom_modifier = models.IntegerField(blank=True, null=True)
    charisma_modifier = models.IntegerField(blank=True, null=True)

    def calculate_modifiers(self):
        #Calculate the ability score modifiers according to D&D 5e rules
        self.strength_modifier = (int(self.strength) - 10) // 2
        self.dexterity_modifier = (int(self.dexterity) - 10) // 2
        self.constitution_modifier = (int(self.constitution) - 10) // 2
        self.intelligence_modifier = (int(self.intelligence) - 10) // 2
        self.wisdom_modifier = (int(self.wisdom) - 10) // 2
        self.charisma_modifier = (int(self.charisma) - 10) // 2