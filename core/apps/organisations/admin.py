from django.contrib import admin
from .models import Organisation, UserOrganisationConnection


@admin.register(Organisation)
class OrganisationAdmin(admin.ModelAdmin):
    list_display = ("title",)


@admin.register(UserOrganisationConnection)
class UserOrganisationConnectionAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "organisation",
    )
    
