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
    # if request.GET.get('btn btn-secondary'):
    #     generated_pk = logic.pick_random_recipe()
    #     meal = Meal.objects.get(pk=generated_pk)
    #     context = {
    #         'meal': meal
    #     }
    # else:
    meal = Meal.objects.get(pk=pk)
    context = {
        'meal': meal
    }

    return render(request, 'meal_detail.html', context)
