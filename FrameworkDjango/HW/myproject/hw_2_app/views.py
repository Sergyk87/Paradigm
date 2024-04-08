from django.shortcuts import render
from django.http import HttpResponse
from .models import User, Product, Order


def index(request):
    return HttpResponse("Hello user!")
