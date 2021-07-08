from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.forms import modelformset_factory
from .models import WRide, WHead
from .forms import WRideForm, WHeadForm

import datetime



def index(request):
    error = ''

    WRideFormset = modelformset_factory(WRide, WRideForm, fields=('time_in', 'time_out', 'route', 'expense_group', 'unit'), 
                                        extra=2)
    
    if request.method == 'POST':
        head_form = WHeadForm(request.POST)
        ride_formset = WRideFormset(request.POST, queryset=WRide.objects.none())
        if head_form.is_valid() and ride_formset.is_valid():
            head_instance = head_form.save(commit=False)
            head_instance.creation_datetime = datetime.datetime.now()
            head_instance = head_form.save()  
            head_id = head_instance.id

            ride_instance = ride_formset.save(commit=False)
            for i in ride_instance:
                i.head_id = head_id

            ride_instance = ride_formset.save()
            return redirect('print_form')

        else:
            error = "Форма заполнена неверно"
    
    else:
        ride_formset = WRideFormset(queryset=WRide.objects.none())
        head_form = WHeadForm()
    data = {
        'head_form' : head_form,
        'ride_formset' : ride_formset,
        'error' : error
    }

    return render(request,'app_main/index.html', data)

def print_form(request):
    return render(request, 'app_main/print_form.html')