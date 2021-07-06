from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import WayBillForm



def index(request):
    error = ''
    if request.method == 'POST':
        form = WayBillForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = "Форма заполнена неверно"
    
    else:
        form = WayBillForm()
    data = {
        'form' : form,
        'error' : error
    }
    return render(request,'app_main/index.html', data)