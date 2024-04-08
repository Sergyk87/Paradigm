from django.db import models
from django.utils import timezone

# Create your models here.


class Coin(models.Model):
    time = models.DateTimeField(default=timezone.now)
    site = models.CharField(max_length=10)

    @staticmethod
    def values():
        value = Coin.objects.order_by("-time")[:5]
        print(value)
        return value

    def __str__(self):
        return f"time: {self.time}, site: {self.site}"
