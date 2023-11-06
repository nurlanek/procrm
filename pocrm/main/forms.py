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
class MasterdataSearchForm(forms.Form):
    start_date = forms.DateField(label='Start Date', required=False)
    end_date = forms.DateField(label='End Date', required=False)
    status_search = forms.CharField(label='Search by Status', required=False)
    kroy_no_search = forms.CharField(label='Search by Kroy_no', required=False)

