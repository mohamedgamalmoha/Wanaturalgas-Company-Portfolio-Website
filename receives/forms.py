from django import forms
from .models import MainRequests


class MainRequestsForm(forms.ModelForm):
    class Meta:
        model = MainRequests
        fields = '__all__'
