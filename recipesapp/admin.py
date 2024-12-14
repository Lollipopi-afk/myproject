from django.contrib import admin
from .models import Categories, RecipeCategory, Recipe

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'cooking_time', 'image')  


admin.site.register(Categories)
admin.site.register(RecipeCategory)
admin.site.register(Recipe)
