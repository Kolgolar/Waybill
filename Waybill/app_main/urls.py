"""
W URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/

Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# Uncomment next two lines to enable admin:
#from django.contrib import admin
from django.urls import path
from . import views

# При получении url запроса вызывает определённую функцию из views.py
urlpatterns = [
    path('', views.index, name='main'),            
    path('get_transport_name', views.get_transport_name, name='get_transport_name'),
    path('get_route_info', views.get_route_info, name='get_route_info'),     
    path('print_page/<form_id>', views.print_page, name='print_page')    
]
