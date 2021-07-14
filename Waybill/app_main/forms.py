from .models import WRide, WHead, Transport
from django.forms import ModelForm, TextInput, modelformset_factory
from django import forms

class WRideForm(ModelForm):
    class Meta:
        model = WRide
        fields = ['time_in', 'time_out', 'route', 'expense_group', 'unit']
        
        widgets={            
            'time_in' : forms.TimeInput(attrs={'style' : 'width:50px'}),
            'time_out' : forms.TimeInput(attrs={
                'style' : 'width:50px', 
                'placeholder' : 'Заполнится автоматически'}),
            'route' : forms.TextInput(attrs={'style' : 'width:50px'}),
            'expense_group' : forms.TextInput(attrs={'style' : 'width:50px'}),
            'unit' : forms.TextInput(attrs={'style' : 'width:50'}),
        }


class WHeadForm(ModelForm):
    class Meta:
        model = WHead
        fields = ['date', 'transport']
        widgets={
            'date' : forms.SelectDateWidget(attrs={'style' : 'width:100px'}),
            'transport' : forms.Select(attrs={'style' : 'width:80px',
                                              'id' : 'tr_id',
                                              'placeholder' : 'Номер ТС'}),
    }
