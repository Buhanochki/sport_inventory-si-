from django.contrib import admin

from core.apps.requests.models import JoinRequest, RepairRequest


@admin.register(JoinRequest)
class JoinRequestAdmin(admin.ModelAdmin):
    list_display = ("user", "organization")


@admin.register(RepairRequest)
class RepairRequestAdmin(admin.ModelAdmin):
    list_display = ("title", "item")
