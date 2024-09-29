from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from .models import Vehicle
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, 'index.html')


def home(request):
    cars = Vehicle.objects.all()

    # Split the images string for each car
    for car in cars:
        car.image_filenames = car.additional_details.images.split(',') if car.additional_details.images else []

    context = {'cars': cars}
    return render(request, 'pages/index.html', context)


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully!')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f'You are now logged in as {username}.')
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.info(request, 'You have successfully logged out.')
    return redirect('login')


def vehicle_detail(request, vehicle_id):
    car = Vehicle.objects.get(id=vehicle_id)
    car.image_filenames = car.additional_details.images.split(',') if car.additional_details.images else []
    context = {'car': car}
    return render(request, 'pages/vehicle_detail.html', context)

def search(request):
    query = request.GET.get('query')
    cars = Vehicle.objects.filter(make__icontains=query)
    context = {'cars': cars}
    return render(request, 'pages/index.html', context)

def all_cars(request):
    cars = Vehicle.objects.all()
    context = {'cars': cars}
    return render(request, 'pages/index.html', context)


def featured_cars(request):
    cars = Vehicle.objects.filter(is_featured=True)
    context = {'cars': cars}
    return render(request, 'pages/index.html', context)

def car_type(request, car_type):
    cars = Vehicle.objects.filter(type=car_type)
    context = {'cars': cars}
    return render(request, 'pages/index.html', context)

def fuel_type(request, fuel_type):
    cars = Vehicle.objects.filter(fuel=fuel_type)
    context = {'cars': cars}
    return render(request, 'pages/index.html', context)

def gearbox_type(request, gearbox_type):
    return render(request, 'pages/index.html')

# Function-based view example
def submit_form(request):
    if request.method == 'POST':
        # Handle the form submission logic here
        return HttpResponse("Form submitted successfully.")
    return redirect('home')