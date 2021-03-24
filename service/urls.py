from . import views
from django.urls import path

app_name = 'service'

urlpatterns = [
    path('heating', views.heating_view, name='heating'),
    path('cooling/', views.cooling_view, name='cooling'),
    path('post/<int:post_id>/', views.post_view, name='post'),
]
