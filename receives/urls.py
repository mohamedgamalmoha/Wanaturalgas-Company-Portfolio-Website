from .views import *
from django.urls import path

app_name = 'receives'

urlpatterns = [
    path('contact-us/', ContactView, name='contact_us'),
    # path('submit-request/', MainRequestView, name='main_form'),
]
