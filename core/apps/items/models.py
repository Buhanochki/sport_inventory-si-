from django.db import models

from core.apps.common.models import TimedBaseModel
from core.apps.users.models import CustomUser


class Item(TimedBaseModel):
    title = models.CharField(max_length=20, verbose_name="Название")
    description = models.TextField(
        verbose_name="Описание",
    )
    picture = models.ImageField(verbose_name="Картинка", upload_to="static/items")

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["pk"]


class UserItemConnection(TimedBaseModel):
    user = models.ForeignKey(CustomUser, verbose_name="Пользователь", on_delete=models.CASCADE)
    item = models.ForeignKey(Item, verbose_name="Продукт", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Пользователь-Продукт"
        ordering = ["pk"]
