from django.http import HttpResponse
from django.shortcuts import render

def mealbuilder(request):
    context = {
        'message': 'Hello, world. You\'re at the mealbuilder index.',
    }
    
    return render(request, 'mealbuilder.html', context=context)