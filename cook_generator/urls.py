from django.urls import path
from . import views

urlpatterns = [
    path("", views.cook_generator_index, name="cook_generator_index"),
    path("<int:pk>/", views.meal_detail, name="meal_detail"),
]