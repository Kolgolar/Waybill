from .models import WayBill
from django.forms import ModelForm, TextInput

class WayBillForm(ModelForm):
    class Meta:
        model = WayBill
        fields = ['date', 'transport', 'time_in', 'time_out', 'route', 'expense_group', 'unit']
        
        widgets = {
            "date": TextInput(attrs={
                'size' : '30%',
                'placeholder' : 'Дата'
            }),
            "transport": TextInput(attrs={
                'placeholder' : 'Номер ТС'
            }),
            "time_in": TextInput(attrs={
                'placeholder' : 'Время прибытия'
            }),
            "time_out": TextInput(attrs={
                'placeholder' : 'Время убытия'
            }),
            "route": TextInput(attrs={
                'placeholder' : 'Номер маршрута'
            }),
            "expense_group": TextInput(attrs={
                'placeholder' : 'Группа расходов'
            }),
            "unit": TextInput(attrs={
                'placeholder' : 'Подразделение'
            }),

            }