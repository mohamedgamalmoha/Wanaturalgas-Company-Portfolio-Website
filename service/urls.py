from . import views
from django.urls import path

app_name = 'service'

urlpatterns = [
    path('heating', views.heating_view, name='heating'),
    path('heating/post/<int:heating_id>/<int:post_id>',
         views.post_heating_view, name='heating_post'),

    path('cooling/', views.cooling_view, name='cooling'),
    path('cooling/post/<int:id1>/<int:id2>',
         views.post_cooling_view, name='cooling_post'),
]
