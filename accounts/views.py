from django.shortcuts import render, redirect
from django.contrib.auth import (
    get_user_model,
    login,
    logout
)
from .forms import UserCreationForm, UserLoginForm

def signup_view(request):
    user = request.user
    if user.is_authenticated:
        return redirect('/')
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/login/')
    return render(request, 'accounts/signup.html', {'form':form})

def login_view(request):
    next = request.POST.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        user_obj = form.cleaned_data.get('user_obj')
        login(request, user_obj)
        if next:
            return redirect(next)
        else:
            return redirect('/')
    return render(request, 'accounts/login.html', {'form':form})


def logout_view(request):
    logout(request)
    return redirect('/login/')