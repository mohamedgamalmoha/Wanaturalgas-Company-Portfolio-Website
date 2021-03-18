from . import views
from django.urls import path

app_name = 'receives'

urlpatterns = [
    path('contact-us/', views.ContactUsPage.as_view(), name='contact_us_page'),
    path('contact-us/send', views.contact_us, name='contact_us'),
    path('success/', views.success, name='contact_us_success'),
    # path('submit-request/', MainRequestView, name='main_form'),
]
