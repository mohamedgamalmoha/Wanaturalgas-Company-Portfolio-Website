from django.urls import path

from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.home_page, name='home'),
    path('about-us/', views.about_page, name='about_us'),
    path('residential/', views.residential_page, name='residential'),
    path('financing/', views.finance_page, name='financing'),
    path('services/', views.services_page, name='services'),
]
