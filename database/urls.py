from django.urls import path, re_path
from .views import view, preview_data

urlpatterns = [
    path("", view),
    path("data/", preview_data, name='data'),
   
]
