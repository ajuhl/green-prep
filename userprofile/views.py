from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import UserForm
from django import template


def profile(request):
    return render(request, 'profile.html')

def profile_edit(request):
    user = request.user
    profile = request.user.profile

    instance = request.user.profile
    form = UserForm(request.POST or None, instance=instance)

    if form.is_valid():
        form.save()
        return redirect('profile')

    return render(request, 'profile_edit.html', {'form': form})

