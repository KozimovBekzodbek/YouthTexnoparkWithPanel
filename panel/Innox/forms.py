from django import forms
from common.models import Registration

class InnoxForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Registration
        fields = (
                "full_name", "gender", "date_birth","address","phone", "startap_name", "category", "another_category", "about_startapp", "about_team","purpose","project_prototype","startap_image" ,"presentation", "agree" 
                )
        widgets = {
            "full_name": forms.TextInput(attrs={"class": "form-control", "language": "all"}),
            "gender": forms.Select(attrs={"class": "form-control"}),
            "date_birth": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "address": forms.TextInput(attrs={"class": "form-control"}),
            "phone": forms.TextInput(attrs={"class": "form-control"}),
            "startap_name": forms.TextInput(attrs={"class": "form-control"}),
            "category": forms.SelectMultiple(attrs={"class": "form-control"}),
            "another_category": forms.TextInput(attrs={"class": "form-control"}),
            "about_startapp": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
            "about_team": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
            "purpose": forms.SelectMultiple(attrs={"class": "form-control"}),
            "project_prototype": forms.Select(attrs={"class": "form-control"}),
            "startap_image": forms.FileInput(attrs={"class": "form-control"}),
            "presentation": forms.FileInput(attrs={"class": "form-control"}),
            "agree": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }


