# Generated by Django 5.1.4 on 2025-01-27 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("items", "0002_remove_item_picture_item_supplier"),
    ]

    operations = [
        migrations.AddField(
            model_name="item",
            name="picture",
            field=models.ImageField(default=1, upload_to="static/items", verbose_name="Картинка"),
            preserve_default=False,
        ),
    ]
