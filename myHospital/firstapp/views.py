from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def home(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())  
def online(request):
    template = loader.get_template('online_consultations.html')
    return HttpResponse(template.render())  
def physical(request):
    template = loader.get_template('physical_appointment.html')
    return HttpResponse(template.render())  
def emergency(request):
    template = loader.get_template('emergency_care.html')
    return HttpResponse(template.render())  