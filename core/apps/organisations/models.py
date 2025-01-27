from django.db import models

from core.apps.common.models import TimedBaseModel
from core.apps.users.models import CustomUser


class Organisation(TimedBaseModel):
    title = models.CharField(verbose_name="Название", max_length=20)

    class Meta:
        verbose_name = "Организация"
        verbose_name_plural = "Организации"
        ordering = ["pk"]

    def __str__(self):
        return f"{self.title}"


class UserOrganisationConnection(TimedBaseModel):
    user = models.ForeignKey(CustomUser, verbose_name="Пользователь", on_delete=models.CASCADE)
    organisation = models.ForeignKey(
        Organisation, verbose_name="Организация", on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Пользователь-Организация"
        ordering = ["pk"]
