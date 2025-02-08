from django import forms

from core.apps.organizations.models import Organization
from core.apps.requests.models import JoinRequest, RepairRequest, CreationRequest


class JoinForm(forms.ModelForm):
    organization = forms.ModelChoiceField(
        queryset=Organization.objects.all(), widget=forms.Select(attrs={"class": "form-control"})
    )

    class Meta:
        model = JoinRequest
        fields = ["organization"]


class RepairForm(forms.ModelForm):
    class Meta:
        model = RepairRequest
        fields = ["title"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "rows": 1}),
        }

class CreationForm(forms.ModelForm):
    class Meta:
        model = CreationRequest
        fields = ["title", "description", "supplier", "amount"]
        widgets = {
                "title": forms.TextInput(attrs={"class": "form-control", "rows": 1}),
                "description": forms.TextInput(attrs={"class": "form-control", "rows": 3}),
                "supplier": forms.TextInput(attrs={"class": "form-control", "rows": 1}),
                "amount": forms.TextInput(attrs={"class": "form-control", "rows": 1}),
            }