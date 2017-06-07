from django import forms
from .models import *
    
    
class AddChannel (forms.ModelForm):
    class Meta:
        model = Channel
        fields = ("name", "number", "rangeMin", "rangeMax", "target", "speed", "acceleration")
        