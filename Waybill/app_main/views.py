from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.forms import modelformset_factory
from .models import WRide, WHead, Transport, Route
from .forms import WRideForm, WHeadForm
from django.utils.timezone import localtime
from django.views.decorators.csrf import csrf_exempt


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
def get_route_desc(request):
    data = {}
    value = (request.GET.dict()["arg"])
    if '/' in value and len(value) > 2:
        idxs = value.split('/')
        obj = Route.objects.all().filter(num_1 = idxs[0], num_2 = idxs[1]).first()
        data = getattr(obj, "description", "Маршрут не найден! Проверьте правильность ввода или введите своё описание.")
    return HttpResponse(data)
       
