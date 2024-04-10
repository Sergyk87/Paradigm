from django.urls import path, include
from .views import index, two_index

urlpatterns = [
    path('', index),
    path('index', two_index),
]
