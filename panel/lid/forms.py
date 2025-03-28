from django import forms
from common.models import CourseContact  

class CourseContactForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = CourseContact
        fields = ("name", "major", "age", "phone_number")

        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Ismingizni kiriting"}),
            "major": forms.Select(attrs={"class": "form-control"}),  
            "age": forms.TextInput(attrs={"class": "form-control", "placeholder": "Yoshingizni kiriting"}),
            "phone_number": forms.TextInput(attrs={"class": "form-control", "placeholder": "+998XXXXXXXXX"}),
        }
