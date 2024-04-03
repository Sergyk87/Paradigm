from django.shortcuts import render

# Create your views here.
import logging
from django.http import HttpResponse

logger = logging.getLogger(__name__)


def index(request):
    html = """
    <body>
        <h1>Главная страница</h1>
            <h2>Мой первый Django-сайт.</ph2>
        <hr>
        <div>
            <p><a href='about_my'>О себе</a></p>
        </div>
    </body>
    """
    logger.info(f"Посещение страницы {__name__}: index")
    return HttpResponse(html)


def about_my(request):
    html = """
    <h1>Коротко о себе)</h1>
    <h2>Привет! Меня зовут Сергей.</h2>
    <hr>
    <div>
        <h2><a href='../'>На главную</a></h2>
    </div>
    """
    logger.info(f"Посещение страницы {__name__}: about")
    return HttpResponse(html)
