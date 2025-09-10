from django import forms
from .models import Organization


class OrganizationForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = ['name', 'college', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }


