# Generated by Django 5.1.4 on 2025-02-08 15:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("organizations", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="JoinRequest",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Дата создания"),
                ),
                ("updated_at", models.DateTimeField(auto_now=True, verbose_name="Дата обновления")),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("IP", "В процессе рассмотрения"),
                            ("DC", "Отклонено"),
                            ("AC", "Принято"),
                        ],
                        default="IP",
                        max_length=2,
                        verbose_name="Статус Заявки",
                    ),
                ),
            ],
            options={
                "verbose_name": "Заявка",
                "verbose_name_plural": "Заявки на вступление",
                "ordering": ["pk"],
            },
        ),
        migrations.CreateModel(
            name="RepairRequest",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Дата создания"),
                ),
                ("updated_at", models.DateTimeField(auto_now=True, verbose_name="Дата обновления")),
                ("title", models.CharField(max_length=20, verbose_name="Название")),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("IP", "В процессе рассмотрения"),
                            ("DC", "Отклонено"),
                            ("AC", "Принято"),
                        ],
                        default="IP",
                        max_length=2,
                        verbose_name="Статус Заявки",
                    ),
                ),
            ],
            options={
                "verbose_name": "Заявка",
                "verbose_name_plural": "Заявки на ремонт",
                "ordering": ["pk"],
            },
        ),
        migrations.CreateModel(
            name="CreationRequest",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Дата создания"),
                ),
                ("updated_at", models.DateTimeField(auto_now=True, verbose_name="Дата обновления")),
                ("title", models.CharField(max_length=20, verbose_name="Название")),
                ("description", models.TextField(verbose_name="Описание")),
                ("supplier", models.CharField(max_length=20, verbose_name="Поставщик")),
                ("amount", models.IntegerField(verbose_name="Количество")),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("IP", "В процессе рассмотрения"),
                            ("DC", "Отклонено"),
                            ("AC", "Принято"),
                        ],
                        default="IP",
                        max_length=2,
                        verbose_name="Статус Заявки",
                    ),
                ),
                (
                    "organization",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="creation_requests",
                        to="organizations.organization",
                    ),
                ),
            ],
            options={
                "verbose_name": "Заявка",
                "verbose_name_plural": "Заявки на создание",
                "ordering": ["pk"],
            },
        ),
    ]
