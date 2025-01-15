from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from .forms import PhysicalAppointmentForm

# Create your views here.

def home(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())  
def online(request):
    template = loader.get_template('online_consultations.html')
    return HttpResponse(template.render())  
def physical(request):
    if request.method == 'POST':
        form = PhysicalAppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('physical_appointment')  # Replace with your success page
    else:
        form = PhysicalAppointmentForm()

    return render(request, 'physical_appointment.html', {'form': form})

def emergency(request):
    template = loader.get_template('emergency_care.html')
    return HttpResponse(template.render())  