from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from random import *
from .models import Coin


def index(request):
    return HttpResponse("Hello world!")


def orel_reshka(request):
    site = choice(["Орел", "Решка"])
    res_orel_reshka = Coin(site=site)
    res_orel_reshka.save()
    return HttpResponse(str(site))


def kub(request):
    return HttpResponse(f"вам выпало: {str(randint(1, 7))}")


def numbers(request):
    return HttpResponse(str(randint(0, 100)))


def coin_values(request):
    value = Coin.values()
    print(value)
    lst = []
    for i in value:
        print(i)
        lst.append(i.site)
    return HttpResponse(lst)
