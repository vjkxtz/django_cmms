from django import forms
from django.forms import ModelForm

from .models import Carrier

class DateInput(forms.DateInput):
    input_type = 'date'

class CarrierForm(ModelForm):
    class Meta:
        model = Carrier
        fields = '__all__'
        widgets = {
            'work_done' : forms.TextInput(attrs={'class': 'form-control'}),
            'changed_date' : DateInput(),
            'created' : DateInput(),
            'front_pickup_trolly' : DateInput(),
            'front_rear_trolly' : DateInput(),
            'rear_pickup_trolly' : DateInput(),
            'rear_nonpickup_trolly' : DateInput(),
            'front_kingpin' : DateInput(),
            'rear_kingpin' : DateInput()
        }