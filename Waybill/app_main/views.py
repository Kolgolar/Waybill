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

# Когда пользователь заполняет и сохраняет форму, django получает данные шапки (она всегда одна) и данные ВСЕХ поездок в одной поездке...
# То есть, как будто бы пользователь не создал n форм, а в каждое поле поездки ввёл n значений

# Шапки и поездки храняться отдельно в БД и объединены общими id (каждая поездка имеет поле head_id)

# Возвращает страницу заполнения формы или перекидывает на страницу печати:
def index(request):
    error = ''

    if request.method == 'POST': # Если пользователь заполнил форму
        head_form = WHeadForm(request.POST) # Получаем введённые значения шапки
        ride_form = WRideForm(request.POST) # Получаем значения ВСЕХ поездок
        #print ride_form
        
        if (head_form.is_valid() and ride_form.is_valid()): #Проверка валидности
            # Создаём запись в БД с шапкой таблицы:
            head_instance = head_form.save(commit=False)
            head_instance.creation_datetime = timezone.now() + timedelta(hours=24)
            head_instance = head_form.save()  
            head_id = head_instance.id # Запоминаем id шапки

            val_q = len(request.POST.getlist("unit")) # Узнаём количество поездок (просто смотрим, сколько значений у полей полученной формы)

            # Создаём список полей поездки (худший код, который я писал, зато если будет меняться структура полей поездки, то ничего менять не надо))))
            all_keys = list(request.POST.dict().keys()) # ВСЕ поля обеих форм
            #TODO: Переделать в цикл
            # Удаляем поля шапки:
            all_keys.remove('csrfmiddlewaretoken')
            all_keys.remove('date_day')            
            all_keys.remove('date_month')
            all_keys.remove('date_year')
            all_keys.remove('transport')
            ride_keys = all_keys # Теперь у нас есть список всех полей поездки

            for i in range(val_q): # Зная количество поездок, сохраняем их в БД
                new_ride = WRide()
                setattr(new_ride, 'head_id', head_id) # Сохраняем id шапки
                for key in ride_keys:
                    setattr(new_ride, key, request.POST.getlist(key)[i])
                new_ride.save()
        else:
            error = "Форма заполнена неверно!"

        return redirect('print_page/' + str(head_id)) # Перевод на страницу печати маршрутного листа, плюс передача id шапки и head_id поездок
    
    # Если пользователь просто перешёл на главную страницу:
    else:
        # Создаём формы:
        head_form = WHeadForm()
        ride_form = WRideForm()
        data = {
            'head_form' : head_form,
            'ride_form' : ride_form,
            'error' : error
        }

        return render(request,'app_main/index.html', data) # Рендерим страницу и передаём данные в html
    

# Возвращает страницу печати:
def print_page(request, form_id):
    head = WHead.objects.get(id = form_id) # Получаем шапку поездки
    rides = WRide.objects.all().filter(head_id = form_id) #Получает QuerySet поездок, относящихся к одному листу
    wb_heads = WHead.objects.all() # Получаем все шапки поездок
    
    #Создаём поле с возможностью выбора любого из ранее созданных листов (НЕ ДОДЕЛАНО):
    ######
    wb_heads_names = ['---------']
    count = 0
    for w in wb_heads:
        date = getattr(w, 'date', 'unknown')
        id = getattr(w, 'id', 'unknown')
        wb_heads_names.append("На " + str(date) + " №" + str(id))
        count += 1    
    wb_list_form = WListForm(wb=wb_heads_names)
    ######
    
    for r in rides: # Проходим по всем поездкам
        route_name = getattr(r, 'route', 'ERROR: Route not found!') # Получаем номер маршрута (не используется в печатной форме)
        description = get_rout_attrs(route_name)['description'] # Используя номер маршрута, получаем его описание
        r.desc = description 
    # Такая наркоманская система используется потому, что в БД каждая поездка хранит только номер маршрута,
    # Соответственно, описание маршрута надо брать из справочника с ними. Вроде логично, но
    # ЖЕЛАТЕЛЬНО ИСПРАВИТЬ ЭТО, поскольку пользователь может вводить своё описание маршрута, но оно не будет сохранено
    # Т.е. надо добавить в модель и форму поездки ещё и поле с описанием маршрута
   
    data = {
        'date' : head.date,
        'transport' : get_tr_data(head.transport),
        'rides' : rides,
        'wb_list_form' : wb_list_form,
    }

    return render(request, 'app_main/print_page.html', data)



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
def get_route_info(request): # Возвращает описание маршрута, время прибытия и убытия
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

def get_rout_attrs(value): # Получаем данные маршрута
    idxs = value.split('/')
    route_obj = Route.objects.all().filter(num_1 = idxs[0], num_2 = idxs[1]).first()
    description = getattr(route_obj, "description", "Маршрут не найден! Проверьте правильность номера или введите своё описание.")
    return {'idxs' : idxs, 'route_obj' : route_obj, 'description' : description}
       
