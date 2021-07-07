from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.forms import modelformset_factory
from .models import WRide, WHead
from .forms import WRideForm, WHeadForm



def index(request):
    error = ''

    WRideFormset = modelformset_factory(WRide, WRideForm, fields=('time_in', 'time_out', 'route', 'expense_group', 'unit'), extra=2)
    
    if request.method == 'POST':
        head_form = WHeadForm(request.POST)
        ride_formset = WRideFormset(request.POST, queryset=WRide.objects.none())
        if head_form.is_valid() and ride_formset.is_valid():
            print(head_form.cleaned_data)
            instances = ride_formset.save()
            instances = head_form.save()           
        else:
            error = "Форма заполнена неверно"
    
    else:
        ride_formset = WRideFormset()
        head_form = WHeadForm()
    data = {
        'head_form' : head_form,
        'ride_formset' : ride_formset,
        'error' : error
    }

    return render(request,'app_main/index.html', data)