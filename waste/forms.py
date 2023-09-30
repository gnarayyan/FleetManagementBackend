from django import forms
from .models import Waste


class WasteForm(forms.ModelForm):
    class Meta:
        model = Waste
        fields = ['latitude', 'longitude', 'waste_volume',
                  'waste_nature', 'image', 'waste_for', 'collection_status']
