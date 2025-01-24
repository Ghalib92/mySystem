from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .forms import PhysicalAppointmentForm
from .models import PhysicalAppointment
from .forms import EmergencyCareForm
from .models import EmergencyCare
from django.core.mail import send_mail
from django.conf import settings
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
           user_email = new_appointment.email  # Field from the model
           subject = 'Booking Confirmation'
           message = (
                f'Dear {new_appointment.name},\n\n'
                f'Your booking has been confirmed. Here are the details:\n\n'
                f'Service: {new_appointment.service_needed}\n'
                 f'Appointment.date: {new_appointment.appointment_date}\n'
                f'Thank you for choosing us!\n\n'
                f'Best regards,\n'
                f'Coast General Hospital'
            )
        from_email = settings.EMAIL_HOST_USER

            # Send the email
        try:
                send_mail(subject, message, from_email, [user_email])
        except Exception as e:
                return render(request, 'email_error.html', {'error': str(e)})

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
    return render(request,'booking_success.html', context)
def emergency(request):
     if request.method == 'POST':
          form = EmergencyCareForm(request.POST)
          if form.is_valid():
               form.save()
               return redirect('emergency_booked')
           
     else:
        form = EmergencyCareForm()

    # If you forgot this line, the view returns None
     return render(request, 'emergency_care.html', {'form': form})
def emergency_booked(request):
     return render(request, 'emergency_booked.html')
 