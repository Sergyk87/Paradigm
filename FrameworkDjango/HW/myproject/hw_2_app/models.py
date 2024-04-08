from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    registration_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return (
            f"Username: {self.name}, email: {self.email}, phone:{self.phone}, "
            f"address: {self.address}, registration_date:{self.registration_date}"
        )


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField()
    date_added = models.DateField(auto_now_add=True)


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    date_ordered = models.DateTimeField(auto_now_add=True)
