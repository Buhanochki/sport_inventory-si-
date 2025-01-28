from django.db import models

from core.apps.common.models import TimedBaseModel
from core.apps.organizations.models import Organization
from core.apps.users.models import CustomUser


class Item(TimedBaseModel):
    title = models.CharField(
        max_length=20,
        verbose_name="Название",
    )
    description = models.TextField(
        verbose_name="Описание",
    )
    picture = models.ImageField(
        verbose_name="Картинка",
        upload_to="static/items",
    )
    supplier = models.CharField(
        max_length=20,
        verbose_name="Поставщик",
    )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["pk"]


class UserItemConnection(TimedBaseModel):
    user = models.ForeignKey(
        CustomUser,
        verbose_name="Пользователь",
        on_delete=models.CASCADE,
        related_name="user_item_connetion",
    )
    item = models.ForeignKey(
        Item,
        verbose_name="Продукт",
        on_delete=models.CASCADE,
        related_name="user_item_connetion",
    )

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Пользователь-Продукт"
        ordering = ["pk"]


class OrganizationItemConnection(TimedBaseModel):
    organization = models.ForeignKey(
        Organization,
        verbose_name="Организация",
        on_delete=models.CASCADE,
        related_name="organisation_item_connection",
    )
    item = models.ForeignKey(
        Item,
        verbose_name="Продукт",
        on_delete=models.CASCADE,
        related_name="organisation_item_connection",
    )
    amount = models.IntegerField(
        verbose_name="Количество",
    )

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Организация-Продукт"
        ordering = ["pk"]
