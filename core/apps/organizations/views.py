from django.shortcuts import redirect, render
from django.views.generic import CreateView

from core.apps.organizations.models import UserOrganizationConnection

from core.apps.organizations.forms import OrganizationCreationForm


class AdminNoOrganization(CreateView):
    template_name = "main/no_organization_admin.html"
    form_class = OrganizationCreationForm
    success_url = "/"

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        if request.user.status != "TC" or UserOrganizationConnection.objects.filter(
            user=request.user
        ):
            return redirect("main-page")
        return render(request, self.template_name, context={"form": form})

    def form_valid(self, form):
        organization = form.instance
        organization.save()
        UserOrganizationConnection.objects.create(
            user=self.request.user, organization=organization
        ).save

        return super().form_valid(form)
