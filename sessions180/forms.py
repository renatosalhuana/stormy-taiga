from django import forms
from .models import Student
from django.utils.translation import gettext_lazy as _


class StudentPresentationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ("name",)
        labels = {
            'name': _('Cuéntame, ¿cuál es tu nombre?')
        }
