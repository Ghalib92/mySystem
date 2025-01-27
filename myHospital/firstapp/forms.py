from django import forms
from .models import PhysicalAppointment
from .models import EmergencyCare
class PhysicalAppointmentForm(forms.ModelForm):
    class Meta:
        model = PhysicalAppointment
        fields = ['name', 'email', 'phone_no', 'service_needed', 'appointment_date']
        widgets = {
            'appointment_date': forms.DateInput(attrs={'type': 'date'}),
        }
class EmergencyCareForm(forms.ModelForm):
    class Meta:
        model = EmergencyCare
        fields = ['patient_name','contact_number','condition_description','priority_level','location']
        widgets = {
            'priority_level': forms.Select(choices=EmergencyCare.priority_level),
            'appointment_date': forms.DateInput(attrs={'type': 'date'}),
        }
        