from django.shortcuts import render
from .forms import WayBillForm

def index(request):
    form = WayBillForm()
    data = {
        'form' : form
    }
    return render(request,'app_main/index.html', data)