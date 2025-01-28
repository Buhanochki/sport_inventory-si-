from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import CreateView, DetailView, ListView, TemplateView

from core.apps.organizations.models import Organization
from core.apps.requests.models import JoinRequest

from core.apps.requests.forms import JoinForm


class JoinRequestCreateView(CreateView):
    template_name = "main/no_organisation_user.html"
    form_class = JoinForm
    success_url = "/dashboard/user"

    def get(self, request, *args, **kwargs):
        if JoinRequest.objects.filter(user=request.user):
            return redirect("join-request-monitor")
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
