from django.shortcuts import render

from service.models import Service
from .models import AboutUs, Residential, Finance, ServicesPage


def home_page(request):
    services = Service.objects.all()
    context = {
        'services': services,
        'active': 'home',
    }
    return render(request, 'home.html', context)


def about_page(request):
    about = AboutUs.objects.all().first()
    context = {
        'about': about,
        'active': 'about',
    }
    return render(request, 'pages/about_us.html', context)


def residential_page(request):
    residential = Residential.objects.all().first()
    context = {
        'residential': residential,
        'active': 'residential',
    }
    return render(request, 'pages/residential.html', context)


def finance_page(request):
    finance = Finance.objects.all().first()
    context = {
        'finance': finance,
        'active': 'financing',
    }
    return render(request, 'pages/finance.html', context)


def services_page(request):
    service = ServicesPage.objects.all().first()
    context = {
        'service': service,
        'active': 'services',
    }
    return render(request, 'pages/services.html', context)
