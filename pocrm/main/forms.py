from django import forms
from .models import Kroy, Kroy_detail, Masterdata

class KroyForm(forms.ModelForm):
    class Meta:
        model = Kroy
        fields = ['kroy_no', 'name', 'ras_tkani', 'ras_dublerin', 'edinitsa', 'description']

class KroyDetailForm(forms.ModelForm):
    class Meta:
        model = Kroy_detail
        fields = ['kroy', 'pachka', 'razmer', 'rost', 'stuk']  # You can specify specific fields if needed

"""class MasterdataForm(forms.ModelForm):
    class Meta:
        model = Masterdata
        fields = ['kroy_no', 'status', 'edinitsa']
"""




