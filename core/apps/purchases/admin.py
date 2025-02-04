from django.contrib import admin
from core.apps.purchases.models import Purchase, PurchaseItem


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ("pk", "title")

@admin.register(PurchaseItem)
class PurchaseItemAdmin(admin.ModelAdmin):
    list_display = ("pk",)