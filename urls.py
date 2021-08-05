from django.urls import path

from home.views import index,details

urlpatterns = [
    path('', index),
    path('details', details),
]