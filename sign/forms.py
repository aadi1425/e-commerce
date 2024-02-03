from django import forms
from .models import *

class Proform(forms.ModelForm):
    class Meta:
        model=Product
        fields='__all__'