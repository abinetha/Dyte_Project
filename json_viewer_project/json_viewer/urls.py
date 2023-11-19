from django.urls import path
from .views import display_json, save_json_data, index, search

urlpatterns = [
    path('display/', display_json, name='display_json'),
    path('save_json_data/', save_json_data, name='save_json_data'),
    path('search/', search, name='search'),
    path('', index, name='index'),
]
