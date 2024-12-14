from django.db import models
from django.contrib.auth.models import User

class Categories(models.Model):
    name = models.CharField(max_length=100, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name 
    

class Recipe(models.Model):
    name = models.CharField(max_length=100, null=False)
    description = models.TextField(null=False)
    cooking_steps = models.TextField(null=False)
    cooking_time = models.DurationField(null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    ingredients = models.TextField(max_length=300, null=False)
    energy_value = models.TextField(max_length=100, null=False)
    categories = models.ManyToManyField(Categories)
    image = models.ImageField(upload_to='recipe_images/', blank=True, null=True)

    def __str__(self):
        return self.name

class RecipeCategory(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)  
    category = models.ForeignKey(Categories, on_delete=models.CASCADE) 

    def __str__(self):
        return f'Рецепт {self.recipe.name} в {self.category.name}'


