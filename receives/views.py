from .forms import MainRequestsForm, ContactForm
from django.shortcuts import render


def ContactView(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
    context = {
        'form': ContactForm,
        'active': 'contact',
    }
    return render(request, 'receives/contact.html', context)


def MainRequestView(request):
    if request.method == 'POST':
        form = MainRequestsForm(request.POST)
        if form.is_valid():
            form.save()
    context = {
        'form': MainRequestsForm
    }
    return render(request, 'receives/main_form.html', context)
