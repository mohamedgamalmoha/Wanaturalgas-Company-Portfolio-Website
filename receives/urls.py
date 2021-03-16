from . import views
from django.urls import path

app_name = 'receives'

urlpatterns = [
    path('contact-us/', views.ContactUsCreate.as_view(), name='contact_us'),
    # path('contact-us/', contact_view, name='contact_us'),
    # path('submit-request/', MainRequestView, name='main_form'),
]
