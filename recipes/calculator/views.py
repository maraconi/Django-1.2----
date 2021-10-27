from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    }
}


def recipe_view(request):
    recipes = list(DATA.keys())
    context = {'recipes': recipes}
    return render(request, template_name='recipe/home.html', context=context)


def ingredients_view(request, recipe):
    if recipe in DATA:
        ingredients = DATA[recipe]
        servings = request.GET.get('servings', None)
        if servings:
            ingredients_list = dict()
            for key, value in ingredients.items():
                ingredients_for_serving = value * int(servings)
                ingredients_list[key] = ingredients_for_serving
            context = {
                'recipe_name': recipe,
                'recipe': ingredients_list
            }
        else:
            context = {
                'recipe_name': recipe,
                'recipe': ingredients
            }
    return render(request, template_name='calculator/index.html', context=context)