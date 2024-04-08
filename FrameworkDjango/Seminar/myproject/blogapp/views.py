from django.http import HttpResponse

from .models import Autor


def index(request):
    return HttpResponse("Hello autor!")


def view_autor(request):
    for i in range(101):
        autor = Autor(
            name=f"aaaa{i}",
            secondname=f"bbbb{i}",
            email=f"aaaa{i}@mail.ru",
            bio=f"cccc{i}",
            bday=f"2023-11-23",
        )
        autor.save()

    return HttpResponse("autor")
