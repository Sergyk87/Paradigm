from django.urls import path
from .views import index, orders_by_customer_id


urlpatterns = [
    path("", index),
    path("user/<int:user_id>/orders/", orders_by_customer_id, name="orders_by_customer_id"),
]