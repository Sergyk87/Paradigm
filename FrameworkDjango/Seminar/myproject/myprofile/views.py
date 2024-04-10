from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    context = {'name': 'Serg', 'lastname': 'H', 'age': 18}
    return render(request, 'myprofile/index.html', context=context)


def two_index(request):
    return render(request, 'myprofile/two_index.html')