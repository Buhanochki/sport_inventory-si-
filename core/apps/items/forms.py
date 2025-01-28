from django import forms

from core.apps.items.models import Item


class ItemCreationForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "rows": 1}))
    description = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "rows": 1})
    )
    supplier = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "rows": 1}))
    amount = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "rows": 1}))


class ItemUpdateForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ["title", "description", "supplier"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "rows": 1}),
            "description": forms.TextInput(attrs={"class": "form-control", "rows": 1}),
            "supplier": forms.TextInput(attrs={"class": "form-control", "rows": 1}),
        }
