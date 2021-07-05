from .models import WayBill, Transport
from django.forms import ModelForm, TextInput

class WayBillForm(ModelForm):
    class Meta:
        model = WayBill
        fields = ['date', 'transport', 'time_in', 'time_out', 'route', 'expense_group', 'unit']
        
       

            