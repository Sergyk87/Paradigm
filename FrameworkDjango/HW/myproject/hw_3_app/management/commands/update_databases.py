from decimal import Decimal
from datetime import timedelta
from random import randint, uniform, choice

from django.utils.timezone import now
from django.core.management.base import BaseCommand

from hw_3_app.models import User, Product, Order


class DBDataError(Exception):
    pass


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument("users_qty", type=int)
        parser.add_argument("products_qty", type=int)
        parser.add_argument("orders_qty", type=int)

    def handle(self, *args, **options):
        users_qty = options.get("users_qty")
        products_qty = options.get("products_qty")
        orders_qty = options.get("orders_qty")

        users_start_counter = len(User.objects.all())
        products_start_counter = len(Product.objects.all())
        orders_start_counter = len(Order.objects.all())

        for i in range(users_start_counter + 1, users_start_counter + users_qty + 1):
            user = User(
                username=f"User_{i}",
                email=f"mail_{i}@mail.ml",
                phone_number=f"+7{''.join([str(randint(0, 9)) for _ in range(10)])}",
                address=f"city{i}",
            )
            user.save()

        for i in range(
            products_start_counter + 1, products_start_counter + products_qty + 1
        ):
            product = Product(
                name=f"Product_{i}e",
                description=f"Description_{i}",
                price=round(uniform(1, 10000), 2),
                quantity=randint(1, 100),
            )
            product.save()

        user = User.objects.all()
        if len(user) == 0:
            raise DBDataError("error")
        products = Product.objects.all()
        if len(products) == 0:
            raise DBDataError("error")

        for i in range(orders_start_counter + 1, orders_start_counter + orders_qty + 1):
            order = Order(
                customer=choice(user),
                total=0,
                time_stamp_on_create=now()
                - timedelta(
                    days=randint(1, 100),
                    hours=randint(1, 23),
                    minutes=randint(0, 59),
                ),
            )
            order.save()
            products_to_order = [choice(products) for _ in range(randint(1, 5))]
            order.products.set(products_to_order)
            order.total = sum([Decimal(i.price) for i in order.products.all()])
            order.save()

        self.stdout.write("ok")
