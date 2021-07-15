from .models import WRide, WHead, Transport, Route
from django.forms import ModelForm, TextInput, modelformset_factory
from django import forms

# Создаёт поле с возможностью как выбора из списка, так и ввода своих значений:
class ListTextWidget(forms.TextInput): 
    def __init__(self, data_list, name, *args, **kwargs):
        super(ListTextWidget, self).__init__(*args, **kwargs)
        self._name = name
        self._list = data_list
        self.attrs.update({'list':'list__%s' % self._name})

    def render(self, name, value, attrs=None, renderer=None):
        text_html = super(ListTextWidget, self).render(name, value, attrs=attrs)
        data_list = '<datalist id="list__%s">' % self._name
        for item in self._list:
            data_list += '<option value="%s">' % item
        data_list += '</datalist>'

        return (text_html + data_list)


class WRideForm(ModelForm):
    class Meta:
        ROUTE_LIST = list(Route.objects.all())

        model = WRide
        fields = ['time_in', 'time_out', 'route', 'expense_group', 'unit']
        
        widgets={            
            'time_in' : forms.TimeInput(attrs={'style' : 'width:50px'}),
            'time_out' : forms.TimeInput(attrs={
                'style' : 'width:50px', 
                'placeholder' : 'Заполнится автоматически'}),
            #'route' : forms.TextInput(attrs={'style' : 'width:50px'}),
            'route' : ListTextWidget(data_list=ROUTE_LIST, name="route_list", attrs={'style' : 'width:50px',
                                                                                     'id' : 'route_id'}),
            'expense_group' : forms.TextInput(attrs={'style' : 'width:50px'}),
            'unit' : forms.TextInput(attrs={'style' : 'width:50'}),
        }


class WHeadForm(ModelForm):
    class Meta:
        TRANSPORT_LIST = list(Transport.objects.all())
        model = WHead
        fields = ['date', 'transport']
        widgets={
            'date' : forms.SelectDateWidget(attrs={'style' : 'width:100px'}),
            'transport' : ListTextWidget(data_list=TRANSPORT_LIST, name="tr_list", attrs={'style' : 'width:80px',
                                                                                      'id' : 'tr_id',
                                                                                      'placeholder' : 'Номер ТС'}),
    }
