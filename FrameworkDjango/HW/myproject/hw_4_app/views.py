from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
import logging

from django.utils.timezone import now
from datetime import timedelta

from hw_4_app.forms import ProductForm
from hw_4_app.models import Customer, Order, Product
from hw_4_app.utils import validator

logger = logging.getLogger(__name__)


def index(request):
    logger.info(f'Посещение страницы {__name__}: index')
    return render(request, 'hw_4_app/index.html')


def about(request):
    logger.info(f'Посещение страницы {__name__}: about')
    return render(request, 'hw_4_app/about.html')


def orders_by_customer_id(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    orders = Order.objects.filter(customer=customer).order_by('-pk')
    context = {'customer': customer, 'orders': orders}
    return render(request, 'hw_4_app/orders_by_customer_id.html', context)


def stats_by_customer_id(request, customer_id, scope_in_days=365):
    scope_dict = {}
    if scope_in_days not in (7, 30, 365):
        scope_dict.setdefault(f'{scope_in_days}', [])
    else:
        scope_dict.update({'7': [], '30': [], '365': []})
    customer = get_object_or_404(Customer, pk=customer_id)
    context = {'customer': customer}
    for k, v in scope_dict.items():
        orders = Order.objects.filter(customer=customer,
                                      time_stamp_on_create__gt=now() - timedelta(days=int(k)))
        # Уберем дубликаты с помощью множества
        products = set([p for o in orders for p in o.products.all()])
        # Вернем список и отсортируем по цене
        products = list(products)
        products.sort(key=lambda x: x.price, reverse=True)
        scope_dict[k].extend(products)
    context['scope_dict'] = scope_dict
    return render(request, 'hw_4_app/stats_by_customer_id.html', context)


def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            if validator.is_value_present_in_db(title, Product, 'title'):
                return HttpResponse(f'Товар с наименованием: "{title}" уже присутствует в БД.')
            product = Product(
                title=form.cleaned_data['title'],
                description=form.cleaned_data['description'],
                price=form.cleaned_data['price'],
                quantity=form.cleaned_data['quantity'],
                time_stamp_on_create=now(),
            )
            product.save()
            logger.info(f'{product} успешно добавлен в базу')
    else:
        form = ProductForm()
    context = {'form': form, 'title': 'Форма создания нового товара'}
    return render(request, 'hw_4_app/create.html', context)


def update_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
    form = ProductForm(instance=product)
    context = {'product': product, 'form': form, 'title': 'Форма обновления данных товара'}
    return render(request, 'hw_4_app/update.html', context)