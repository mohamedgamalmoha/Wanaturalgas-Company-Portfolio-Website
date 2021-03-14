from .views import *
from django.urls import path

app_name = 'receives'

urlpatterns = [
    path('contact', ContactView, name='contact'),
    path('main_form', MainRequestView, name='main_form'),
]
