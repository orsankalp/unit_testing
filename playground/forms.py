from django import forms
from .models import contact
class DateInput(forms.DateInput):
    input_type = 'date'
class contactForm(forms.ModelForm):
    class Meta:
        model = contact
        fields = '__all__'
      
    