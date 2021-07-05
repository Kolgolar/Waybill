from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import WayBillForm



def index(request):
    if request.method == 'POST':
        form = WayBillForm(request.POST)
        if form.is_valid():

            return HttpResponseRedirect('')
    
    else:
        form = WayBillForm()
    data = {
        'form' : form,
    }
    return render(request,'app_main/index.html', data)