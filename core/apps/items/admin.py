from django.contrib import admin

from core.apps.items.models import Item, OrganizationItemConnection, UserItemConnection


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "created_at",
        "updated_at",
    )


@admin.register(UserItemConnection)
class UserItemConnectionAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "item",
        "created_at",
        "updated_at",
    )


@admin.register(OrganizationItemConnection)
class OrganizationItemConnectionAdmin(admin.ModelAdmin):
    list_display = (
        "organization",
        "item",
        "created_at",
        "updated_at",
    )
