from django.db import models

from core.apps.common.models import TimedBaseModel
from core.apps.items.models import Item
from core.apps.organizations.models import Organization
from core.apps.users.models import CustomUser


class JoinRequest(TimedBaseModel):
    user = models.ForeignKey(
        CustomUser,
        verbose_name="Пользователь",
        on_delete=models.CASCADE,
        related_name="join_requests",
    )
    organization = models.ForeignKey(
        Organization,
        verbose_name="Организация",
        on_delete=models.CASCADE,
        related_name="join_requests",
    )

    STATUS_CHOICES = [
        ("IP", "В процессе рассмотрения"),
        ("DC", "Отклонено"),
        ("AC", "Принято"),
    ]
    status = models.CharField(
        verbose_name="Статус Заявки",
        choices=STATUS_CHOICES,
        max_length=2,
        default="IP",
    )

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки на вступление"
        ordering = ["pk"]


class CreationRequest(TimedBaseModel):
    title = models.CharField(
        max_length=20,
        verbose_name="Название",
    )
    description = models.TextField(
        verbose_name="Описание",
    )
    supplier = models.CharField(
        max_length=20,
        verbose_name="Поставщик",
    )
    amount = models.IntegerField(
        verbose_name="Количество"
    )
    STATUS_CHOICES = [
        ("IP", "В процессе рассмотрения"),
        ("DC", "Отклонено"),
        ("AC", "Принято"),
    ]
    status = models.CharField(
        verbose_name="Статус Заявки",
        choices=STATUS_CHOICES,
        max_length=2,
        default="IP",
    )
    user = models.ForeignKey(
        CustomUser,
        verbose_name="Пользователь",
        on_delete=models.CASCADE,
        related_name="creation_requests",
    )
    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name="creation_requests",
    )

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки на создание"
        ordering = ["pk"]

class RepairRequest(TimedBaseModel):
    title = models.CharField(
        max_length=20,
        verbose_name="Название",
    )
    user = models.ForeignKey(
        CustomUser,
        verbose_name="Пользователь",
        on_delete=models.CASCADE,
        related_name="repair_requests",
    )
    item = models.ForeignKey(
        Item,
        on_delete=models.CASCADE,
        related_name="repair_requests",
    )
    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name="repair_requests",
    )
    STATUS_CHOICES = [
        ("IP", "В процессе рассмотрения"),
        ("DC", "Отклонено"),
        ("AC", "Принято"),
    ]
    status = models.CharField(
        verbose_name="Статус Заявки",
        choices=STATUS_CHOICES,
        max_length=2,
        default="IP",
    )

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки на ремонт"
        ordering = ["pk"]
