from django.urls import path
from .views import update_data, get_latest_data

urlpatterns = [
    path('update_data/', update_data, name='update_data'),
    path('get_latest_data/', get_latest_data, name='get_latest_data'),
]