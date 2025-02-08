# Generated by Django 5.1.4 on 2025-02-08 15:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("items", "0001_initial"),
        ("organizations", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="organizationitemconnection",
            name="organization",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="organisation_item_connection",
                to="organizations.organization",
                verbose_name="Организация",
            ),
        ),
        migrations.AddField(
            model_name="useritemconnection",
            name="item",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="user_item_connetion",
                to="items.item",
                verbose_name="Продукт",
            ),
        ),
    ]
