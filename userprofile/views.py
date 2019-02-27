from django.http import HttpResponse
from django.shortcuts import render

def profile(request):
    return HttpResponse("Hello, world. You're at the user profile page.")