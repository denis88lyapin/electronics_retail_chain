# Generated by Django 5.0 on 2023-12-22 18:17

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="network",
            options={"verbose_name": "Сеть", "verbose_name_plural": "Сети"},
        ),
    ]
