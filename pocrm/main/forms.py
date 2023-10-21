from django import forms
from .models import Kroy, Kroy_detail

class KroyForm(forms.ModelForm):
    class Meta:
        model = Kroy
        fields = '__all__'  # You can specify specific fields if needed

class KroyDetailForm(forms.ModelForm):
    class Meta:
        model = Kroy_detail
        fields = '__all__'  # You can specify specific fields if needed
