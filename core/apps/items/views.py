from django.shortcuts import HttpResponseRedirect, redirect, render
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    TemplateView,
    UpdateView,
)

from core.apps.items.models import Item, OrganizationItemConnection, UserItemConnection
from core.apps.organizations.models import UserOrganizationConnection

from core.apps.items.forms import ItemCreationForm, ItemUpdateForm


class AdminItemsListView(ListView):
    model = OrganizationItemConnection
    template_name = "main_page/admin.html"
    context_object_name = "items"

    def get(self, request, *args, **kwargs):
        if self.request.user.is_anonymous:
            return redirect("login")
        if not self.request.user.status == "TC":
            return redirect("user-dashboard")
        if not UserOrganizationConnection.objects.filter(user=self.request.user):
            return redirect("join-request")

        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if UserOrganizationConnection.objects.filter(user=self.request.user):
            context["items"] = OrganizationItemConnection.objects.filter(
                organization=UserOrganizationConnection.objects.get(
                    user=self.request.user
                ).organization
            )
        return context


class UserItemsListView(ListView):
    model = OrganizationItemConnection
    template_name = "main_page/user.html"
    context_object_name = "items"

    def get(self, request, *args, **kwargs):
        if self.request.user.is_anonymous:
            return redirect("login")
        if not self.request.user.status == "PT":
            return redirect("admin-dashboard")
        if not UserOrganizationConnection.objects.filter(user=self.request.user):
            return redirect("join-request")

        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if UserOrganizationConnection.objects.filter(user=self.request.user):
            context["items"] = OrganizationItemConnection.objects.filter(
                organization=UserOrganizationConnection.objects.get(
                    user=self.request.user
                ).organization
            )
        context["user_inventory"] = [
            item.item for item in UserItemConnection.objects.filter(user=self.request.user)
        ]
        print(context["user_inventory"])
        return context


class ItemCreateView(TemplateView):
    template_name = "items/create.html"
    form_class = ItemCreationForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        if request.user.status == "TC" and not request.user.is_anonymous:
            return render(request, self.template_name, context={"form": form})
        return redirect("main-page")

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            item = Item.objects.create(
                title=form.cleaned_data.get("title"),
                description=form.cleaned_data.get("description"),
                supplier=form.cleaned_data.get("supplier"),
            )
            OrganizationItemConnection.objects.create(
                organization=UserOrganizationConnection.objects.get(
                    user=self.request.user
                ).organization,
                item=item,
                amount=form.cleaned_data.get("amount"),
            ).save()
            item.save()
            return redirect("main-page")
        return render(request, self.template_name, context={"form": form})


class ItemUpdateView(UpdateView):
    model = Item
    form_class = ItemUpdateForm
    template_name = "items/update.html"
    context_object_name = "item"
    success_url = "/dashboard/admin"

    def get(self, request, *args, **kwargs):
        if request.user.status == "TC" and not request.user.is_anonymous:
            return super().get(request, *args, **kwargs)
        return redirect("main-page")


class ItemDetailedView(DetailView):
    model = Item
    template_name = "items/detailed.html"
    context_object_name = "item"


class UserInventory(ListView):
    model = UserItemConnection
    template_name = "items/user.html"
    context_object_name = "items"

    def get(self, request, *args, **kwargs):
        if request.user.status == "PT" and not request.user.is_anonymous:
            return super().get(request, *args, **kwargs)
        return redirect('main-page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["items"] = UserItemConnection.objects.filter(user=self.request.user)
        return context


def item_delete(request, pk):
    if request.user.status == "TC" and not request.user.is_anonymous:
        object = Item.objects.get(pk=pk)
        organization_item = OrganizationItemConnection.objects.get(item=object)
        object.delete()
        organization_item.delete()

        return HttpResponseRedirect(request.META["HTTP_REFERER"])
    return redirect("main-page")


def item_rent(request, pk):
    if request.user.status == "PT" and not request.user.is_anonymous:
        object = OrganizationItemConnection.objects.get(pk=pk)
        object.amount -= 1
        object.save()
        UserItemConnection.objects.create(user=request.user, item=object.item).save()
        return HttpResponseRedirect(request.META["HTTP_REFERER"])
    return redirect("main-page")


def cancel_rent(request, pk):
    if request.user.status == "PT" and not request.user.is_anonymous:
        object = UserItemConnection.objects.get(pk=pk)
        organization_item = OrganizationItemConnection.objects.get(item=object.item)
        organization_item.amount += 1
        organization_item.save()
        object.delete()
        return HttpResponseRedirect(request.META["HTTP_REFERER"])
    return redirect("main-page")
