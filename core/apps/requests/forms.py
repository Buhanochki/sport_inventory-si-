from django import forms

from core.apps.organizations.models import Organization
from core.apps.requests.models import JoinRequest, RepairRequest


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
