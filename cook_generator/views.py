from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from cook_generator.models import Meal


def cook_generator_index(request):
    """
    Func to render main page
    :param request:
    :return:
    """
    meals = Meal.objects.all()
    context = {
        'meals': meals,
        'carousel': meals
    }
    return render(request, 'cook_generator_index.html', context)


def meal_detail(request, pk):
    meal = Meal.objects.get(pk=pk)
    context = {
        'meal': meal
    }
    return render(request, 'meal_detail.html', context)
