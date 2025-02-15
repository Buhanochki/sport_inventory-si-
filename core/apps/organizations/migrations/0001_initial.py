# Generated by Django 5.1.4 on 2025-02-08 15:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Organization",
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
            ],
            options={
                "verbose_name": "Организация",
                "verbose_name_plural": "Организации",
                "ordering": ["pk"],
            },
        ),
        migrations.CreateModel(
            name="UserOrganizationConnection",
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
                    "organization",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_organisation_connection",
                        to="organizations.organization",
                        verbose_name="Организация",
                    ),
                ),
            ],
            options={
                "verbose_name": "Запись",
                "verbose_name_plural": "Пользователь-Организация",
                "ordering": ["pk"],
            },
        ),
    ]
