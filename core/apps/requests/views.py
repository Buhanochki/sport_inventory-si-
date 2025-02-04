from django.shortcuts import HttpResponseRedirect, get_object_or_404, redirect, render
from django.views.generic import CreateView, DetailView, ListView, TemplateView

from core.apps.items.models import Item, OrganizationItemConnection, UserItemConnection
from core.apps.organizations.models import Organization, UserOrganizationConnection
from core.apps.requests.models import JoinRequest, RepairRequest

from core.apps.requests.forms import JoinForm, RepairForm


class JoinRequestCreateView(CreateView):
    template_name = "main/no_organisation_user.html"
    form_class = JoinForm
    success_url = "/dashboard/user"

    def get(self, request, *args, **kwargs):
        if JoinRequest.objects.filter(user=request.user):
            return redirect("join-request-monitor")
        if request.user.status == "TC":
            return redirect("organization-create")
        if UserOrganizationConnection.objects.filter(user=request.user):
            return redirect('main-page')
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
    template_name = "main/admin_join_requests.html"
    context_object_name = "requests"

    def get(self, request, *args, **kwargs):
        if request.user.status == "TC":
            return super().get(request, *args, **kwargs)
        return redirect('main-page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["requests"] = JoinRequest.objects.filter(
            organization=UserOrganizationConnection.objects.get(user=self.request.user).organization
        )
        return context


class RepairRequestAdminListView(ListView):
    model = RepairRequest
    template_name = "main/admin_repair_requests.html"
    context_object_name = "requests"

    def get(self, request, *args, **kwargs):
        if request.user.status == "TC":
            return super().get(request, *args, **kwargs)
        return redirect('main-page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["requests"] = RepairRequest.objects.filter(
            organization=UserOrganizationConnection.objects.get(user=self.request.user).organization
        )
        return context


class RepairRequestListView(ListView):
    model = RepairRequest
    context_object_name = "requests"
    template_name = "main/user_repair_requests.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["requests"] = RepairRequest.objects.filter(user=self.request.user)
        return context


class RepairRequestCreateView(CreateView):
    model = RepairRequest
    form_class = RepairForm
    template_name = "main/repair_request_create.html"
    success_url = "/items/inventory/user"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["pk"] = self.kwargs.get("pk")
        return context

    def form_valid(self, form):
        item = Item.objects.get(pk=self.kwargs.get("pk"))
        form.instance.item = item
        form.instance.organization = UserOrganizationConnection.objects.get(
            user=self.request.user
        ).organization
        form.instance.user = self.request.user
        form.instance.save()
        UserItemConnection.objects.get(user=self.request.user, item=item).delete()

        return super().form_valid(form)


def join_request_decline(request, pk):
    if request.user.status == "TC":
        joinrequest = JoinRequest.objects.get(pk=pk)
        joinrequest.status = "DC"
        joinrequest.save()

        return HttpResponseRedirect(request.META["HTTP_REFERER"])
    return redirect("main-page")


def join_request_accept(request, pk):
    if request.user.status == "TC":
        joinrequest = JoinRequest.objects.get(pk=pk)
        if not UserOrganizationConnection.objects.filter(user=joinrequest.user):
            joinrequest.status = "AC"
            joinrequest.save()
            UserOrganizationConnection.objects.create(
                organization=joinrequest.organization, user=joinrequest.user
            ).save()
            return HttpResponseRedirect(request.META["HTTP_REFERER"])
        return redirect("requests-admin-join-decline", pk)
    return redirect("main-page")


def repair_request_decline(request, pk):
    if request.user.status == "TC":
        repairrequest = RepairRequest.objects.get(pk=pk)
        repairrequest.status = "DC"
        repairrequest.save()
        item_organization = OrganizationItemConnection.objects.get(item=repairrequest.item)
        item_organization.amount += 1
        item_organization.save()

        return HttpResponseRedirect(request.META["HTTP_REFERER"])
    return redirect("main-page")


def repair_request_accept(request, pk):
    if request.user.status == "TC":
        repairrequest = RepairRequest.objects.get(pk=pk)
        repairrequest.status = "AC"
        repairrequest.save()
        item_organization = OrganizationItemConnection.objects.get(item=repairrequest.item)
        item_organization.amount += 1
        item_organization.save()

        return HttpResponseRedirect(request.META["HTTP_REFERER"])
    return redirect("main-page")
