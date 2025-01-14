from django import forms
from .models import PhysicalAppointment

class PhysicalAppointmentForm(forms.ModelForm):
    class Meta:
        model = PhysicalAppointment
        fields = ['name', 'email', 'phone_no', 'service_needed', 'appointment_date']
        widgets = {
            'appointment_date': forms.DateInput(attrs={'type': 'date'}),
        }
