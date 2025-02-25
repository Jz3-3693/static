from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout

# Login page view
def login(request):
    return render(request, 'login.html')

# Home page view
def home(request):
    return render(request, 'home.html')

# Index page view
def index(request):
    return render(request, 'index.html')

# Register view
def register_view(request):
    if request.method == "POST":
        username = request.POST.get('rusnm')
        email = request.POST.get('remail')
        password = request.POST.get('regpass')
        
        # Check if username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return redirect('register_view')
        else:
            # Create user and save to db
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            messages.success(request, 'Account successfully created. Please login!')
            return redirect('login_view')
    
    return render(request, 'login.html', {'form_type': 'register'})

# Login view
def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Authenticate User
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Incorrect username or password')
    
    return render(request, 'login.html', {'form_type': 'login'})

# Logout view
def logout_view(request):
    logout(request)
    messages.success(request, 'Successfully logged out')
    return redirect('login')