from django import forms
from common.models import ServiceContact  

class ServiceContactForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = ServiceContact
        fields = ("name", "phone_number")

        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Ismingizni kiriting"}),
            "phone_number": forms.TextInput(attrs={"class": "form-control", "placeholder": "+998XXXXXXXXX"}),
        }
