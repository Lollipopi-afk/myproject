from django import forms
from .models import Recipe



class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'description', 'cooking_steps', 'cooking_time', 'ingredients', 'energy_value', 'categories', 'image']
