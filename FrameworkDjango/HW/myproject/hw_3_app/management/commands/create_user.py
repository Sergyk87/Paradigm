from django.core.management.base import BaseCommand
from hw_3_app.models import User


class Command(BaseCommand):
    help = "Create user."

    def handle(self, *args, **kwargs):
        user = User(
            name="Serg", email="sergyk@ya.ru", phone="+7-999-999-99-99", address="City"
        )
        user.save()
        self.stdout.write(f"{user}")
