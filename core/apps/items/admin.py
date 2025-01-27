from django.contrib import admin

from .models import Item, OrganisationItemConnection, UserItemConnection


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


@admin.register(OrganisationItemConnection)
class OrganisationItemConnectionAdmin(admin.ModelAdmin):
    list_display = (
        "organisation",
        "item",
        "created_at",
        "updated_at",
    )
