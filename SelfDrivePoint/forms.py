from django import forms
from .models import SelfDrivePoint


class PointCreateForm(forms.ModelForm):
    class Meta:
        model=SelfDrivePoint
        fields = ['order_no', 'order_time', 'phone_no', 'is_installed','point','creator','city']
