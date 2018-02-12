from django import forms
from .models import *

class BronForm(forms.ModelForm):
    class Meta:
        model = Bron
        exclude = [""]
