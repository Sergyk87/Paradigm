from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello world!")

def about_my(request):
    return HttpResponse("Привет! Меня зовут Сергей")
