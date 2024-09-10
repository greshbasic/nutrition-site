from django.shortcuts import render
from django.http import JsonResponse
from .form import FoodForm
from .nutrition import NutritionInfo

def index(request):
    if request.method == 'POST':
        form = FoodForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            info = NutritionInfo(name)
            calories = info.get_calories()  # Assuming this method performs the API call
            print(f"calories: {calories}")
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':  # Check if the request is AJAX
                return JsonResponse({'calories': calories})
            return render(request, 'index.html', {'form': form, 'calories': calories})
    else:
        form = FoodForm()

    return render(request, 'index.html', {'form': form})