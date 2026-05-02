from django.urls import path
from . import views

urlpatterns = [
    path('',                                    views.home,            name='home'),
    path('recipes/',                            views.recipe_list,     name='recipe_list'),
    path('recipes/<slug:slug>/',                views.recipe_detail,   name='recipe_detail'),
    path('recipes/<slug:slug>/save/',           views.toggle_save,     name='toggle_save'),
    path('recipes/<slug:slug>/rate/',           views.rate_recipe,     name='rate_recipe'),
    path('recipes/<slug:slug>/translation/',    views.get_translation, name='get_translation'),
    path('state/<slug:slug>/',                  views.state_detail,    name='state_detail'),
    path('cuisine/<slug:slug>/',                views.cuisine_detail,  name='cuisine_detail'),
    path('category/<slug:slug>/',               views.category_detail, name='category_detail'),
]
