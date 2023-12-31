# Generated by Django 4.2.3 on 2023-07-16 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Recipes",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=128)),
                ("description", models.CharField(max_length=1024)),
                ("time", models.DateField(auto_now_add=True)),
                (
                    "category",
                    models.CharField(
                        choices=[("SA", "Салаты"), ("CO", "Коктейли"), ("PA", "Паста")],
                        default="SA",
                        max_length=2,
                    ),
                ),
            ],
        ),
    ]
