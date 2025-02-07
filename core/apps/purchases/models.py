from django.db import models
from core.apps.common.models import TimedBaseModel
from core.apps.items.models import Item
from core.apps.organizations.models import Organization


class Purchase(TimedBaseModel):
    title = models.CharField(max_length=20, verbose_name="Название")
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, verbose_name="Организация")
    item = models.ForeignKey(Item, on_delete=models.CASCADE, verbose_name="Предмет")
    amount = models.IntegerField(verbose_name="Количество")
    

    
    