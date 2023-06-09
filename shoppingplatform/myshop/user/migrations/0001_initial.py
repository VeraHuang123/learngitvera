# Generated by Django 4.2.1 on 2023-06-01 07:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("created_at", models.DateTimeField(auto_now=True)),
                ("updated_at", models.DateTimeField(auto_now_add=True)),
                ("company", models.CharField(max_length=200)),
                ("email", models.CharField(max_length=200)),
                ("password", models.CharField(max_length=200)),
                ("first_name", models.CharField(max_length=200)),
                ("last_name", models.CharField(max_length=200)),
                ("phone", models.CharField(max_length=200)),
                ("store_credit", models.IntegerField(default=0)),
                ("registration_ip_address", models.CharField(max_length=200)),
                (
                    "customer_group_id",
                    models.IntegerField(
                        default=0,
                        validators=[django.core.validators.MinValueValidator(0)],
                    ),
                ),
                ("notes", models.CharField(max_length=200)),
                ("tax_exempt_category", models.CharField(max_length=200)),
            ],
            options={
                "db_table": "user",
            },
        ),
    ]
