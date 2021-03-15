from django.urls import path

from .views import *

app_name = 'pages'

urlpatterns = [
    path('', home_page, name='home'),
    path('about-us/', about_page, name='about_us'),
    path('residential/', residential_page, name='residential'),
    path('financing/', finance_page, name='financing'),
]
