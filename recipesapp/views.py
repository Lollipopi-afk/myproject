from django.shortcuts import render, get_object_or_404, reverse
from .models import Recipe
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


def index(request):
    recipes = Recipe.objects.all() 
    return render(request, 'recipesapp/recipe-index.html', {'recipes': recipes})

def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'recipesapp/recipe_detail.html', {'recipe': recipe})

def all_recipes(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipesapp/all_recipes.html', {'recipes': recipes})

@method_decorator(login_required, name='dispatch')
class RecipeCreateView(CreateView):
    model = Recipe
    fields = ['name', 'description', 'cooking_steps', 'cooking_time', 'ingredients', 'energy_value', 'categories', 'image']
    template_name = 'recipesapp/create_recipe.html'
    success_url = reverse_lazy('recipesapp:all_recipes')

    def form_valid(self, form):
        form.instance.author = self.request.user 
        return super().form_valid(form)

    def form_invalid(self, form):
        print("Form invalid")
        print(form.errors) 
        return super().form_invalid(form)
    

class RecipeUpdateView(UpdateView): 
    model = Recipe  
    fields = ['name', 'description', 'cooking_steps', 'cooking_time', 'ingredients', 'energy_value', 'image', 'categories']  
    template_name_suffix = '_update_form' 

    def get_success_url(self): 
        return reverse(
            'recipesapp:recipe_detail',
            kwargs={'pk': self.object.pk}, 
        )