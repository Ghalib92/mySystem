from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .forms import PhysicalAppointmentForm
from .models import PhysicalAppointment

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
           new_appointment= form.save()
           return redirect('booking_success',appointment_id=new_appointment.id)  # Replace with your success page
    else:
        form = PhysicalAppointmentForm()

    return render(request, 'physical_appointment.html', {'form': form})
def booking(request,appointment_id):
    appointment = get_object_or_404(PhysicalAppointment, id=appointment_id)
    
    context = {
        'service':appointment.name,
        'appointment_date':appointment.appointment_date,
        'email': appointment.email

 }
    return render(request, 'booking_success.html', context)
def emergency(request):
    template = loader.get_template('emergency_care.html')
    return HttpResponse(template.render())  
 