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
        route_list = list(Route.objects.all())
        print(route_list)

        model = WRide
        fields = ['time_in', 'time_out', 'route', 'expense_group', 'unit']
        
        widgets={            
<<<<<<< Updated upstream
            'time_in' : forms.TimeInput(attrs={'style' : 'width:50px'}),
            'time_out' : forms.TimeInput(attrs={
                'style' : 'width:50px', 
                'placeholder' : 'Заполнится автоматически'}),
            #'route' : forms.TextInput(attrs={'style' : 'width:50px'}),
            'route' : ListTextWidget(data_list=route_list, name="route_list", attrs={'style' : 'width:50px',
                                                                                     'id' : 'route_id'}),
            'expense_group' : forms.TextInput(attrs={'style' : 'width:50px'}),
            'unit' : forms.TextInput(attrs={'style' : 'width:50'}),
=======
            'time_in' : forms.TimeInput(attrs={
                                            'style' : 'width:50px',
                                            'class' : 'time_in_class',
                                            'id' : 'time_in'}),

            'time_out' : forms.TimeInput(attrs={
                                            'style' : 'width:50px', 
                                            'placeholder' : 'Заполнится автоматически',
                                            'class' : 'time_out_class',
                                            'id' : 'time_out'}),

            'route' : ListTextWidget(data_list=ROUTE_LIST, name="route_list", 
                                         attrs={
                                            'style' : 'width:130px',
                                            'id' : 'route_id',
                                            'placeholder' : '№ маршрута',
                                            'class' : 'route_id_class'}),

            'expense_group' : ListTextWidget(data_list=EXPENSE_GROUP_LIST, name="expense_group_list",
                                        attrs={
                                            'style' : 'width:80px',
                                            'class' : 'table_center_field'}),
            
            'unit' : ListTextWidget(data_list=UNIT_LIST, name="unit_list",
                                        attrs={
                                            'style' : 'width:50',
                                            'class' : 'table_center_field'}),
>>>>>>> Stashed changes
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
