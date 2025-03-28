from django import forms
from .models import Registration, CourseContact

class InnoxForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields ="__all__"


class CourseContactForm(forms.ModelForm):
    class Meta:
        model = CourseContact
        fields = '__all__'