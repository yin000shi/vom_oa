from django import forms
from .models import Nporder


class NporderCreateForm(forms.ModelForm):
    class Meta:
        model=Nporder
        fields = ['order_no', 'vin', 'creator', 'city']
