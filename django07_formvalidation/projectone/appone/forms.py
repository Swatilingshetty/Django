from typing import Any
from django import forms
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.core import validators

# custom validators
def validate_name(value):
    if not value.isupper():
        raise ValidationError(f'{value} is not in uppercase')
    
class userprofileform(forms.Form):

    first_name=forms.CharField(validators=[validate_name,validators.MinLengthValidator(3)])
    last_name=forms.CharField(validators=[validate_name,validators.MinLengthValidator(3)])
    email=forms.EmailField()
    # phone_regex=r'^\d{1,12}$'
    # phone=forms.CharField(validators=[RegexValidator(phone_regex)])
    phone=forms.CharField()
    comment=forms.CharField(widget=forms.Textarea)
    LOCATION=[{"HYD","hyderabad"},{"Bnglr","Bangalore"}]
    location=forms.CharField(widget=forms.Select(choices=LOCATION))
    join_date=forms.DateField(widget=forms.SelectDateWidget)

    def clean_first_name(self):
        first_name= self.cleaned_data["first_name"]
        if not first_name.isalpha():
            raise forms.ValidationError("first name should be contain only alphabet")
        return first_name
    
    def clean_last_name(self):
        last_name= self.cleaned_data["last_name"]
        if not last_name.isalpha():
            raise forms.ValidationError("last name should be contain only alphabet")
        return last_name
    
    def clean(self):
        cleaned_data=super().clean()
        first_name=cleaned_data.get('first_name')
        last_name=cleaned_data.get('last_name')
        if first_name and last_name:
            if first_name==last_name:
             raise forms.ValidationError("ffirst name and last name cannot be same")
            
    def clean_email(self):
        email=self.cleaned_data['email']
        if not email.endswith('@mail.com'):
            raise forms.ValidationError("email should be gmail")
        return email
