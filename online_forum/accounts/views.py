from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from .services import register_user, authenticate_user
from django.core.exceptions import ValidationError

def home(request):
    return render(request, 'accounts/base.html')  # main landing page

@csrf_exempt
def register_view(request):
    if request.method == 'POST':
        try:
            data = {
                'username': request.POST.get('username'),
                'email': request.POST.get('email'),
                'password': request.POST.get('password'),
            }
            user = register_user(data)
            messages.success(request, f"User {user.username} registered successfully.")
            return redirect('login')  # or to homepage
        except ValidationError as e:
            messages.error(request, str(e))
        except Exception as e:
            messages.error(request, str(e))
    return render(request, 'accounts/register.html')

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        try:
            data = {
                'username': request.POST.get('username'),
                'password': request.POST.get('password'),
            }
            user = authenticate_user(data)
            if user:
                messages.success(request, f"Welcome back, {user.username}!")
                return redirect('home')  # or wherever you want
            else:
                messages.error(request, "Invalid credentials.")
        except Exception as e:
            messages.error(request, str(e))
    return render(request, 'accounts/login.html')
