from django.shortcuts import render, get_object_or_404
from django.utils.timezone import now
from datetime import timedelta
from .models import User, Product, Order


def index(request):
    return render(request, "hw_3_app/index.html")


def orders_by_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    orders = Order.objects.filter(user=user).all()
    context = {"user": user, "orders": orders}
    return render(request, "hw_3_app/orders_by_user.html", context)


def statistics_by_user(request, user_id, scope_in_days=365):
    scope_dict = {}
    if scope_in_days not in (7, 30, 365):
        scope_dict.setdefault(f"{scope_in_days}", [])
    else:
        scope_dict.update({"7": [], "30": [], "365": []})
    user = get_object_or_404(User, pk=user_id)
    context = {"user_id": user_id}
    for k, v in scope_dict.items():
        orders = Order.objects.filter(
            user_id=user_id, time_stamp_on_create__gt=now() - timedelta(days=int(k))
        )
        products = set([p for o in orders for p in o.products.all()])
        products = list(products)
        products.sort(key=lambda x: x.price, reverse=True)
        scope_dict[k].extend(products)
    context["scope_dict"] = scope_dict
    return render(request, "hw_3_app/statistics_by_user.html", context)
