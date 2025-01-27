from django.db import models
from core.apps.common.models import TimedBaseModel
from core.apps.users.models import CustomUser
from core.apps.organisations.models import Organisation
from core.apps.items.models import Item


class JoinRequest(TimedBaseModel):
    user = models.ForeignKey(
        CustomUser,
        verbose_name="Пользователь",
        on_delete=models.CASCADE
    )
    organisation = models.ForeignKey(
        Organisation,
        verbose_name="Организация",
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки на вступление"
        ordering = ["pk"]


class RepairRequest(TimedBaseModel):
    title = models.CharField(
        max_length=20,
        verbose_name="Название",
    )
    item = models.ForeignKey(
        Item,
        on_delete=models.CASCADE
    )
    organisation = models.ForeignKey(
        Organisation,
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки на ремонт"
        ordering = ["pk"]
