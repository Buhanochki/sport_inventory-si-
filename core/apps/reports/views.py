from core.apps.requests.models import RepairRequest
from core.apps.items.models import OrganizationItemConnection, UserItemConnection
from core.apps.organizations.models import UserOrganizationConnection
from django.views.generic import ListView
from django.shortcuts import redirect


class InUseReport(ListView):
    model = UserItemConnection
    template_name = 'reports/in_use.html'
    context_object_name = 'requests'

    def get(self, request, *args, **kwargs):
        if request.user.status == "TC" and not request.user.is_anonymous:
            return super().get(request, *args, **kwargs)
        return redirect('main-page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        organization = UserOrganizationConnection.objects.get(user=self.request.user).organization
        users = UserOrganizationConnection.objects.filter(organization=organization).values_list('user')
        context['requests'] = UserItemConnection.objects.filter(user__in=users)
        context['amount'] = len(context['requests'])
        context['organization_title'] = organization.title
        return context
    

class BrokenReport(ListView):
    model = RepairRequest
    context_object_name = "requests"
    template_name = 'reports/broken.html'

    def get(self, request, *args, **kwargs):
        if request.user.status == "TC" and not request.user.is_anonymous:
            return super().get(request, *args, **kwargs)
        return redirect('main-page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['organization_title'] = UserOrganizationConnection.objects.get(user=self.request.user).organization.title
        return context
    
    def get_queryset(self):
        return super().get_queryset().filter(organization=UserOrganizationConnection.objects.get(user=self.request.user).organization, status="IP")
    

class NewReport(ListView):
    model = OrganizationItemConnection
    context_object_name = 'requests'
    template_name = 'reports/new.html'

    def get(self, request, *args, **kwargs):
        if request.user.status == "TC" and not request.user.is_anonymous:
            return super().get(request, *args, **kwargs)
        return redirect('main-page')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['organization_title'] = UserOrganizationConnection.objects.get(user=self.request.user).organization.title
        return context
    
    def get_queryset(self):
        return super().get_queryset().filter(organization=UserOrganizationConnection.objects.get(user=self.request.user).organization)

    