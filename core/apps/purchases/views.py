from django.shortcuts import render
from django.views.generic import ListView
from core.apps.purchases.models import Purchase


class PurchasesListView(ListView):
    model = Purchase
    context_object_name = "purchases"
    template_name = "main/purchases_view.html"