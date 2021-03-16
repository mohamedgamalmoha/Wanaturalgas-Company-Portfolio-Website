from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.messages.views import SuccessMessageMixin

from .forms import MainRequestsForm, ContactForm
from .models import Contact


class ContactUsCreate(SuccessMessageMixin, CreateView):
    model = Contact
    template_name = 'receives/contact.html'
    success_url = reverse_lazy('receives:contact_us')
    success_message = 'Thank you for contacting us, we will get back to you as soon as possible.'
    form_class = ContactForm

    def get_context_data(self, **kwargs):
        context = super(ContactUsCreate, self).get_context_data(**kwargs)
        context['active'] = 'contact'
        return context


def MainRequestView(request):
    if request.method == 'POST':
        form = MainRequestsForm(request.POST)
        if form.is_valid():
            form.save()
    context = {
        'form': MainRequestsForm
    }
    return render(request, 'receives/main_form.html', context)
