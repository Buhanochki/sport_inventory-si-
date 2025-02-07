from django.views.generic import ListView, CreateView
from core.apps.purchases.models import Purchase
from core.apps.organizations.models import UserOrganizationConnection
from core.apps.purchases.forms import PurchaseCreateForm
from django.shortcuts import redirect, HttpResponseRedirect


class PurchasesListView(ListView):
    model = Purchase
    context_object_name = "purchases"
    template_name = "purchases/view.html"

    def get(self, request, *args, **kwargs):
        if request.user.status == "TC" and not request.user.is_anonymous:
            return super().get(request, *args, **kwargs)
        return redirect('main-page')

    def get_queryset(self):
        return super().get_queryset().filter(organization=UserOrganizationConnection.objects.get(user=self.request.user).organization)
    

class PurchasesCreateView(CreateView):
    form_class = PurchaseCreateForm
    template_name = "purchases/create.html"
    success_url = "/purchases/view"

    def get(self, request, *args, **kwargs):
        if request.user.status == "TC" and not request.user.is_anonymous:
            return super().get(request, *args, **kwargs)
        return redirect('main-page')

    def form_valid(self, form):
        form.instance.organization = UserOrganizationConnection.objects.get(user=self.request.user).organization
        form.instance.save()
        return super().form_valid(form)
    

def purchase_delete(request, pk):
    if request.user.status == "TC" and not request.user.is_anonymous:
        object = Purchase.objects.get(pk=pk)
        object.delete()

        return HttpResponseRedirect(request.META["HTTP_REFERER"])
    return redirect("main-page")