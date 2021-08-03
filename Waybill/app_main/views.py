from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.forms import modelformset_factory
from .models import WRide, WHead, Transport, Route, InlineStop
from .forms import WRideForm, WHeadForm, WListForm
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
    print(request.method)
    if request.method == 'POST':
        head_form = WHeadForm(request.POST)
        ride_form = WRideForm(request.POST)
        if (head_form.is_valid() and ride_form.is_valid()):
            head_instance = head_form.save(commit=False)
            head_instance.creation_datetime = timezone.now() + timedelta(hours=24)
            head_instance = head_form.save()  
            head_id = head_instance.id

            val_q = len(request.POST.getlist("unit"))

            all_keys = list(request.POST.dict().keys())
            #TODO: Remove fields with cycle
            all_keys.remove('csrfmiddlewaretoken')
            all_keys.remove('date_day')            
            all_keys.remove('date_month')
            all_keys.remove('date_year')
            all_keys.remove('transport')
            ride_keys = all_keys
            #print(ride_keys)

            for i in range(val_q):
                new_ride = WRide()
                setattr(new_ride, 'head_id', head_id)
                for key in ride_keys:
                    setattr(new_ride, key, request.POST.getlist(key)[i])
                    #print(("Form #{0}, field '{1}' = {2}").format(i, key, new_ride.key)) #Не работает
                new_ride.save()
        else:
            error = "Форма заполнена неверно!"

        #return redirect('print_form')

        return redirect('print_page/' + str(head_id))
    
    else:
        head_form = WHeadForm()
        ride_form = WRideForm()
        data = {
            'head_form' : head_form,
            'ride_form' : ride_form,
            'error' : error
        }

        return render(request,'app_main/index.html', data)
    

def print_page(request, form_id):
    head = WHead.objects.get(id = form_id)
    rides = WRide.objects.all().filter(head_id = form_id) #Получает QuerySet поездок, относящихся к одному листу
    wb_heads = WHead.objects.all()
    
    #Создаём поле с возможностью выбора любого из ранее созданных листов:
    wb_heads_names = ['---------']
    count = 0
    for w in wb_heads:
        date = getattr(w, 'date', 'unknown')
        id = getattr(w, 'id', 'unknown')
        wb_heads_names.append("На " + str(date) + " №" + str(id))
        count += 1    
    wb_list_form = WListForm(wb=wb_heads_names)

    for r in rides:
        route_name = getattr(r, 'route', 'ERROR: Route not found!')
        description = get_rout_attrs(route_name)['description']
        r.desc = description
   
    data = {
        'date' : head.date,
        'transport' : get_tr_data(head.transport),
        'rides' : rides,
        'wb_list_form' : wb_list_form,
    }

    return render(request, 'app_main/print_page.html', data)


def print_form(request):
    return render(request, 'app_main/print_form.html')


#TODO: Передавать на клиент отдельно марку и номер, создавать строку уже там
def get_transport_name(request): # Вызывается через JQuery
    id = (request.GET.dict()["arg"])
    data = get_tr_data(id)
    return HttpResponse(data)


def get_tr_data(id_need): # Собственно логика получения номера и имени ТС
    obj = Transport.objects.get(id = id_need)  
    mark = getattr(obj, "mark", "Not found")
    plate = getattr(obj, "plate", "Not found")
    data = ("{0}   {1}").format(mark, plate.upper())
    return data


#TODO: Сделать проверку валидности строки на стороне клиента
def get_route_info(request):
    data = {}
    description = ''
    time_in = 0
    time_out = 0
    value = (request.GET.dict()["arg"])
    if '/' in value and len(value) > 2:

        attr = get_rout_attrs(value)
        idxs = attr['idxs']
        route_obj = attr['route_obj']
        description = attr['description']      

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

def get_rout_attrs(value):
    idxs = value.split('/')
    route_obj = Route.objects.all().filter(num_1 = idxs[0], num_2 = idxs[1]).first()
    description = getattr(route_obj, "description", "Маршрут не найден! Проверьте правильность номера или введите своё описание.")
    return {'idxs' : idxs, 'route_obj' : route_obj, 'description' : description}
       
