from django.contrib import admin
from core.apps.purchases.models import Purchase


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ("pk", "title")

