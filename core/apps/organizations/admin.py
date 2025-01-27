from django.contrib import admin

from core.apps.organizations.models import Organization, UserOrganizationConnection


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ("title",)


@admin.register(UserOrganizationConnection)
class UserOrganizationConnectionAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "organization",
    )
