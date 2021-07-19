from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.forms import modelformset_factory
from .models import WRide, WHead, Transport, Route, InlineStop
from .forms import WRideForm, WHeadForm
from django.utils.timezone import localtime
from django.views.decorators.csrf import csrf_exempt
import json
import datetime


from django.utils import timezone
from datetime import timedelta


@csrf_exempt

def index(request):
    error = ''
    HEAD_FIELDS_Q = 3
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
            #TODO: Remove fields and make cycle
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
        else:
            error = "Форма заполнена неверно!"


        return redirect('print_form')
    else:
        head_form = WHeadForm()
        ride_form = WRideForm()
        data = {
            'head_form' : head_form,
            'ride_form' : ride_form,
            'error' : error
        }

        return render(request,'app_main/index.html', data)
    

def print_form(request):
    return render(request, 'app_main/print_form.html')

#TODO: Передавать на клиент отдельно марку и номер, создавать строку уже там
def get_transport_name(request):    
    value = (request.GET.dict()["arg"])
    obj = Transport.objects.get(id = value)  
    mark = getattr(obj, "mark", "Not found")
    plate = getattr(obj, "plate", "Not found")
    data = ("{0}   {1}").format(mark, plate.upper())
    return HttpResponse(data)


#TODO: Сделать проверку валидности строки на стороне клиента
def get_route_info(request):
    data = {}
    description = ''
    time_in = 0
    time_out = 0
    value = (request.GET.dict()["arg"])
    if '/' in value and len(value) > 2:
        idxs = value.split('/')
        route_obj = Route.objects.all().filter(num_1 = idxs[0], num_2 = idxs[1]).first()
        description = getattr(route_obj, "description", "Маршрут не найден! Проверьте правильность ввода или введите своё описание.")
        
        time_in_obj = InlineStop.objects.all().filter(route_id = route_obj.id).first()
        t = getattr(time_in_obj, "time", 303)
        time_in = t.hour * 60 + t.minute

        time_out_obj = InlineStop.objects.all().filter(route_id = route_obj.id).last()
        t = getattr(time_out_obj, "time", 404)
        print(t)
        time_out = t.hour * 60 + t.minute
    
    data = {
        'description' : description,
        'time_in' : time_in,
        'time_out' : time_out
    }
    data_json = json.dumps(data)
    return HttpResponse(data_json)
       
