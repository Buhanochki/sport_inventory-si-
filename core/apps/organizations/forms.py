from django import forms
from core.apps.organizations.models import Organization


class OrganizationCreationForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = ['title']
        widgets = {
            'title': forms.TextInput(attrs={"class":"form-control"})
        }