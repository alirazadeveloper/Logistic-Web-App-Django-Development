from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home.html', {})


def dashboard(request):
    return render(request, 'dashboard.html', {})


def MyShipments(request):
    return render(request, 'MyShipments.html', {})


def MyConsolidations(request):
    return render(request, 'MyConsolidations.html', {})
