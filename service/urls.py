from .views import HeatingView, CoolingView, PostHeatingView, PostCoolingView
from django.urls import path

app_name = 'service'

urlpatterns = [
    path('heating', HeatingView, name='heating'),
    path('heating/post/<int:heating_id>/<int:post_id>', PostHeatingView, name='heating_post'),

    path('cooling', CoolingView, name='cooling'),
    path('cooling/post/<int:id1>/<int:id2>>', PostCoolingView, name='cooling_post'),
]
