# Generated by Django 5.0.3 on 2024-04-14 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("hw_3_app", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="order",
            old_name="customer",
            new_name="user",
        ),
    ]
