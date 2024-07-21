from django import forms
from appone.models import product

class productform(forms.ModelForm):
    class Meta:
        model=product
        fields='__all__'