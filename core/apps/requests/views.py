from django.shortcuts import get_object_or_404, redirect, render, HttpResponseRedirect
from django.views.generic import CreateView, DetailView, ListView, TemplateView

from core.apps.organizations.models import Organization, UserOrganizationConnection
from core.apps.requests.models import JoinRequest

from core.apps.requests.forms import JoinForm


class JoinRequestCreateView(CreateView):
    template_name = "main/no_organisation_user.html"
    form_class = JoinForm
    success_url = "/dashboard/user"

    def get(self, request, *args, **kwargs):
        if JoinRequest.objects.filter(user=request.user):
            return redirect("join-request-monitor")
        if request.user.status == "TC":
            return redirect('organization-create')
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        if not JoinRequest.objects.filter(user=self.request.user):
            form.instance.user = self.request.user
            form.instance.save()
            return super().form_valid(form)
        return redirect("join-request-monitor")


class JoinRequestMonitor(DetailView):
    template_name = "main/join_request_monitor.html"
    model = JoinRequest
    context_object_name = "request"

    def get_object(self, queryset=None):
        return get_object_or_404(JoinRequest, user=self.request.user)


class JoinRequestAdminListView(ListView):
    model = JoinRequest
    template_name = 'main/admin_join_requests.html'
    context_object_name = 'requests'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['requests'] = JoinRequest.objects.filter(organization=UserOrganizationConnection.objects.get(user=self.request.user).organization)
        return context

def join_request_decline(request, pk):
    if request.user.status == "TC":
        joinrequest = JoinRequest.objects.get(pk=pk)
        joinrequest.status = "DC"
        joinrequest.save()

        return HttpResponseRedirect(request.META["HTTP_REFERER"])
    return redirect('main-page')

def join_request_accept(request, pk):
    if request.user.status == "TC":
        joinrequest = JoinRequest.objects.get(pk=pk)
        if not UserOrganizationConnection.objects.filter(user=joinrequest.user): 
            joinrequest.status = "AC"
            joinrequest.save()
            UserOrganizationConnection.objects.create(organization=joinrequest.organization, user=joinrequest.user).save()
            return HttpResponseRedirect(request.META["HTTP_REFERER"])
        return redirect('requests-admin-join-decline', pk)
    return redirect('main-page')
        
