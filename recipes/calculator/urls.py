from django.contrib import admin
from django.urls import path, include
from .views import recipe_view, ingredients_view

urlpatterns = [
    path('', recipe_view, name='home'),
    path('<recipe>/', ingredients_view, name='recipe')
]