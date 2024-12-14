from django.urls import path, include
from .views import index
from .views import recipe_detail, all_recipes, RecipeCreateView, RecipeUpdateView

app_name = "recipesapp"


urlpatterns = [
    path('', index, name='index'), 
    path('detail/<int:pk>/', recipe_detail, name='recipe_detail'),
    path('all/', all_recipes, name='all_recipes'),
    path('create/recipe/', RecipeCreateView.as_view(), name='create_recipe'),
    path('<int:pk>/update/', RecipeUpdateView.as_view(), name='update_recipe'),
]
