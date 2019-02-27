from django.http import HttpResponse
from django.shortcuts import render

def list(request):
    context = {
        'message': 'Hello, world. You\'re at the grocery list index.',
    }
    
    return render(request, 'grocerylist.html', context=context)