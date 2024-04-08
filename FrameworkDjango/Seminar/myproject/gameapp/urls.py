"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from .views import index, kub, orel_reshka, numbers, coin_values

urlpatterns = [
    path("", index, name="index"),
    path("kub", kub, name="kub"),
    path("orel_reshka", orel_reshka, name="orel_reshka"),
    path("numbers", numbers, name="numbers"),
    path("coin_values", coin_values, name="coin_values"),
]
