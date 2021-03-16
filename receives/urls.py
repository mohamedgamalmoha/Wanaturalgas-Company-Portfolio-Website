from .views import *
from django.urls import path

app_name = 'receives'

urlpatterns = [
    path('contact-us/', ContactUsCreate.as_view(), name='contact_us'),
    # path('contact-us/', contact_view, name='contact_us'),
    # path('submit-request/', MainRequestView, name='main_form'),
]
