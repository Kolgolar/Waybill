from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.forms import modelformset_factory
from .models import WRide, WHead
from .forms import WRideForm, WHeadForm
from django.utils.timezone import localtime
from django.views.decorators.csrf import csrf_exempt


from django.utils import timezone
from datetime import timedelta

formset_q = 1
HEAD_FIELDS_Q = 3

@csrf_exempt

def index(request):
    if request.method == 'POST':
        head_form = WHeadForm(request.POST)
        ride_form = WRideForm(request.POST)
        if (head_form.is_valid() and ride_form.is_valid()):
            head_instance = head_form.save(commit=False)
            head_instance.creation_datetime = timezone.now() + timedelta(hours=24)
            head_instance = head_form.save()  
            head_id = head_instance.id

            val_q = len(request.POST.getlist("unit"))

            ride_keys = list(request.POST.dict().keys())
            #TODO: Remove fields in cycle
            ride_keys.remove('csrfmiddlewaretoken')
            ride_keys.remove('date_day')            
            ride_keys.remove('date_month')
            ride_keys.remove('date_year')
            ride_keys.remove('transport')
            #print(ride_keys)

            for i in range(val_q):
                new_ride_form = WRideForm(request.POST)
                for key in ride_keys:
                    instance = new_ride_form.save(commit=False)
                    instance.key = request.POST.getlist(key)[i]                    
                    print(("Form #{0}, field '{1}' = {2}").format(i, key, instance.key))
                instance.head_id = head_id
                instance = new_ride_form.save()
        return redirect('print_form')
    else:
        head_form = WHeadForm()
        ride_form = WRideForm()
        data = {
            'head_form' : head_form,
            'ride_formset' : ride_form,
        }

        return render(request,'app_main/index.html', data)


def index_old(request):
    error = ''
    WRideFormset = modelformset_factory(WRide, WRideForm, fields=('time_in', 'time_out', 'route', 'expense_group', 'unit'), 
                                        extra=1)
    
    if request.method == 'POST':
        head_form = WHeadForm(request.POST)
        ride_formset = WRideForm(request.POST)
        print(ride_formset)
        if head_form.is_valid() and ride_formset.is_valid():
            head_instance = head_form.save(commit=False)
            head_instance.creation_datetime = timezone.now() + timedelta(hours=24)
            head_instance = head_form.save()  
            head_id = head_instance.id

            ride_instance = ride_formset.save(commit=False)
            #for i in ride_instance:
            #    i.head_id = head_id
            ride_instance.head_id = head_id

            ride_instance = ride_formset.save()
            return redirect('print_form')

        else:
            error = "Форма заполнена неверно"
    
    else:
        ride_formset = WRideForm()
        head_form = WHeadForm()
    data = {
        'head_form' : head_form,
        'ride_formset' : ride_formset,
        'error' : error
    }

    return render(request,'app_main/index.html', data)
    

def print_form(request):
    return render(request, 'app_main/print_form.html')


def size_changing(request, value):
    global formset_q
    new_formset_q = formset_q + value
    if (new_formset_q > 0 and new_formset_q < 5):
        formset_q += value
    else:
        print('Некорректное значение строк!')
    return redirect('main')


def add_formset(request):
    return size_changing(request, 1)

def remove_formset(request):
    return size_changing(request, -1)