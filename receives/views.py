from django.contrib import messages
from django.shortcuts import redirect, render

from django.views.generic import TemplateView, CreateView

from .forms import ContactForm
from .models import Contact, MainRequests


class ContactUsPage(TemplateView):
    template_name = 'receives/contact.html'

    def get_context_data(self, **kwargs):
        context = super(ContactUsPage, self).get_context_data(**kwargs)
        context['active'] = 'contact'
        return context


def contact_us(request):
    Question = request.POST.get('Question')
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    emil_address = request.POST.get('emil_address')

    zip_code = request.POST.get('zip_code')
    phone_number = request.POST.get('phone_number')
    
    if first_name and emil_address and Question and zip_code and phone_number:
        contact = Contact(
            first_name=first_name,
            last_name=last_name,
            Question=Question,
            emil_address=emil_address,
            zip_code=zip_code,
            phone_number=phone_number,
            )
        contact.save()
        msg = "Thank you for contacting us, we will get back to you as soon as possible."
        messages.success(request, msg)           
    else:
        msg = "something went wrong , please try again later."
        messages.error(request, msg)
    return redirect("receives:contact_us_success")


def success(request):
    return render(request, "receives/success.html", {})


class ContactUsView(CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'receives/contact_us.html'
    success_url = '/'


class MainRequestView(CreateView):
    model = MainRequests
    fields = '__all__'
    template_name = 'receives/main_form.html'
    success_url = '/'

