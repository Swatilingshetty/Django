from django import forms
from appone.models import Userprofile

class userprofileform(forms.ModelForm):

    class Meta:
        model=Userprofile
        fields='__all__'
