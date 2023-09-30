from django.shortcuts import render, redirect
from .models import SoilData, Profile
from .forms import SignUpForm, SoilDataForm
from django.contrib.auth import authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    profiles = Profile.objects.all()
    soils = SoilData.objects.all()

    context = {
        'profiles': profiles,
        'soils': soils,
    }
    return render(request, 'index.html', context=context)

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            messages.success(request, 'Registration successful.')
            return redirect('index')
        messages.error(request, 'Unsuccessful registration. Invalid information.')
    form = SignUpForm()
    return render(request, 'registration/register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('index')
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'login_form': form})

def logout_view(request):
    auth_logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('index')

@login_required
def soil_data(request):
    if request.method == 'POST':
        form = SoilDataForm(request.POST)
        if form.is_valid():
            try:
                data = form.save(commit=False)
                data.user = request.user
                data.save()
                return redirect('user_dashboard')
            except Exception as e:
                return render(request, 'soil_data.html', {'form': form, 'error': e})
        else:
            return render(request, 'soil_data.html', {'form': form, 'error_message': 'Form validation failed.'})
    else:
        form = SoilDataForm()
    return render(request, 'soil_data.html', {'form': form})

@login_required
def user_dashboard(request):
    soil_data = SoilData.objects.filter(user=request.user)
    # Implement logic to calculate health assessments if needed
    return render(request, 'dashboard.html', {'soil_data': soil_data})
