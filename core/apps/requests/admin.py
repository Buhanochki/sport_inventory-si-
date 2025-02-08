from django.contrib import admin

from core.apps.requests.models import JoinRequest, RepairRequest, CreationRequest


@admin.register(JoinRequest)
class JoinRequestAdmin(admin.ModelAdmin):
    list_display = ("user", "organization", "status")


@admin.register(RepairRequest)
class RepairRequestAdmin(admin.ModelAdmin):
    list_display = ("title", "item", "status")

@admin.register(CreationRequest)
class RepairRequestAdmin(admin.ModelAdmin):
    list_display = ("title", "status")

