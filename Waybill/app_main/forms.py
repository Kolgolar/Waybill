from .models import WayBill, Transport
from django.forms import ModelForm, TextInput
from django import forms

class WayBillForm(ModelForm):
    class Meta:
        model = WayBill
        fields = ['date', 'transport', 'time_in', 'time_out', 'route', 'expense_group', 'unit']
        
        widgets={
            'date' : forms.SelectDateWidget(attrs={'style' : 'width:100px'}),
            'transport' : forms.Select(attrs={'style' : 'width:300px'}),
            'time_in' : forms.TextInput(attrs={'style' : 'width:300px'}),
            'time_out' : forms.TimeInput(attrs={
                'style' : 'width:300px', 
                'placeholder' : 'Заполнится автоматически'}),
            'route' : forms.TextInput(attrs={'style' : 'width:300px'}),
            'expense_group' : forms.TextInput(attrs={'style' : 'width:300px'}),
            'unit' : forms.TextInput(attrs={'style' : 'width:300px'})
        }
       

            