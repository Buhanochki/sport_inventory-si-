from django.shortcuts import HttpResponseRedirect, get_object_or_404, redirect
from django.views.generic import CreateView, DetailView, ListView

from core.apps.items.models import Item, OrganizationItemConnection, UserItemConnection
from core.apps.organizations.models import UserOrganizationConnection
from core.apps.requests.models import CreationRequest, JoinRequest, RepairRequest

from core.apps.requests.forms import CreationForm, JoinForm, RepairForm


class JoinRequestCreateView(CreateView):
    template_name = "requests/join_create.html"
    form_class = JoinForm
    success_url = "/dashboard/user"

    def get(self, request, *args, **kwargs):
        if JoinRequest.objects.filter(user=request.user):
            return redirect("join-request-monitor")
        if request.user.status == "TC":
            return redirect("organization-create")
        if UserOrganizationConnection.objects.filter(user=request.user):
            return redirect("main-page")
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        if not JoinRequest.objects.filter(user=self.request.user):
            form.instance.user = self.request.user
            form.instance.save()
            return super().form_valid(form)
        return redirect("join-request-monitor")


class JoinRequestMonitor(DetailView):
    template_name = "requests/join_monitor.html"
    model = JoinRequest
    context_object_name = "request"

    def get_object(self, queryset=None):
        return get_object_or_404(JoinRequest, user=self.request.user)


class JoinRequestAdminListView(ListView):
    model = JoinRequest
    template_name = "requests/join_admin.html"
    context_object_name = "requests"

    def get(self, request, *args, **kwargs):
        if request.user.status == "TC" and not request.user.is_anonymous:
            return super().get(request, *args, **kwargs)
        return redirect("main-page")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["requests"] = JoinRequest.objects.filter(
            organization=UserOrganizationConnection.objects.get(user=self.request.user).organization
        )
        return context


class RepairRequestAdminListView(ListView):
    model = RepairRequest
    template_name = "requests/repair_admin.html"
    context_object_name = "requests"

    def get(self, request, *args, **kwargs):
        if request.user.status == "TC" and not request.user.is_anonymous:
            return super().get(request, *args, **kwargs)
        return redirect("main-page")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["requests"] = RepairRequest.objects.filter(
            organization=UserOrganizationConnection.objects.get(user=self.request.user).organization
        )
        return context


class RepairRequestListView(ListView):
    model = RepairRequest
    context_object_name = "requests"
    template_name = "requests/user.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["requests"] = RepairRequest.objects.filter(user=self.request.user)
        return context


class RepairRequestCreateView(CreateView):
    model = RepairRequest
    form_class = RepairForm
    template_name = "requests/repair_create.html"
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


class CreationRequestCreateView(CreateView):
    model = CreationRequest
    template_name = "requests/creation_create.html"
    form_class = CreationForm
    success_url = "/"

    def form_valid(self, form):
        form.instance.organization = UserOrganizationConnection.objects.get(
            user=self.request.user
        ).organization
        form.instance.user = self.request.user
        form.instance.save()
        return super().form_valid(form)


class CreationRequestListView(ListView):
    model = CreationRequest
    context_object_name = "requests"
    template_name = "requests/creation_view.html"

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


class AdminCreationRequestListView(ListView):
    model = CreationRequest
    context_object_name = "requests"
    template_name = "requests/create_admin.html"

    def get_queryset(self):
        return (
            super()
            .get_queryset()
            .filter(
                organization=UserOrganizationConnection.objects.get(
                    user=self.request.user
                ).organization
            )
        )


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


def creation_request_accept(request, pk):
    if request.user.status == "TC":
        creationrequest = CreationRequest.objects.get(pk=pk)
        creationrequest.status = "AC"
        creationrequest.save()
        item = Item.objects.create(
            title=creationrequest.title,
            description=creationrequest.description,
            supplier=creationrequest.supplier,
        )
        item.save()
        item_organization = OrganizationItemConnection.objects.create(
            organization=creationrequest.organization, item=item, amount=creationrequest.amount
        )
        item_organization.save()

    return redirect("main-page")


def creation_request_decline(request, pk):
    if request.user.status == "TC":
        creationrequest = CreationRequest.objects.get(pk=pk)
        creationrequest.status = "DC"
        creationrequest.save()

    return redirect("main-page")
