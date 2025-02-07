from django import forms
from core.apps.purchases.models import Purchase
from core.apps.items.models import Item


class PurchaseCreateForm(forms.ModelForm):
    item = forms.ModelChoiceField(
        queryset=Item.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
    )
    class Meta:
        model = Purchase
        fields = ['title', 'amount', 'item']
        widgets = {
            'title': forms.TextInput(attrs={"class":"form-control", "placeholder":"Введите название"}),
            'amount': forms.TextInput(attrs={"class":"form-control", "placeholder":"Введите количество"})
        }