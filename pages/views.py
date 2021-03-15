from django.shortcuts import render

from .models import About, Residential, Finance

def home_page(request):
    context = {
        'active':'home',
    }
    return render(request, 'home.html', context)


def about_page(request):
    about = About.objects.all().first()
    context = {
        'about':about,
        'active':'about',
    }
    return render(request, 'pages/about_us.html', context)


def residential_page(request):
    residential = Residential.objects.all().first()
    context = {
        'residential':residential,
        'active':'residential',
    }
    return render(request, 'pages/residential.html', context)

def finance_page(request):
    finance = Finance.objects.all().first()
    context = {
        'finance':finance,
        'active':'financing',
    }
    return render(request, 'pages/finance.html', context)
