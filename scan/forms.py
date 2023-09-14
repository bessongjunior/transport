from django import forms
from .models import BarcodeData

class BarcodeForm(forms.ModelForm):
    class Meta:
        model = BarcodeData
        fields = [
            'barcode_number', 
            'longitude',
            'latitude',
            # 'user'
            ]