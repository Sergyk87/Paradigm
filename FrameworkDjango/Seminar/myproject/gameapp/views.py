from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from random import *
from .models import Coin


def index(request):
    return HttpResponse("Hello world!")


# def orel_reshka(request):
#     site = choice(["Орел", "Решка"])
#     res_orel_reshka = Coin(site=site)
#     res_orel_reshka.save()
#     return HttpResponse(str(site))


def kub(request, count):
    lst = []
    for i in range(count):
        num = randint(1, 7)
        lst.append(num)
    context = {'game_name': 'Кубик', 'value': lst}
    return render(request, 'gameapp/game.html', context)


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


def orel_reshka(request, count=5):
    lst = []
    for i in range(count):
        site = choice(["Орел", "Решка"])
        lst.append(site)
    context = {'game_name': 'Орел или решка', 'value': lst}
    return render(request, 'gameapp/game.html', context)
