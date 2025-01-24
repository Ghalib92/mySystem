from django.contrib import admin
from .models import PhysicalAppointment
from .models import EmergencyCare

# Register your models here.
# admin.py
 

@admin.register(PhysicalAppointment)
class PhysicalAppointmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_no', 'service_needed', 'appointment_date', 'created_at')
    search_fields = ('name', 'email', 'phone_no', 'service_needed')
    list_filter = ('service_needed', 'appointment_date')
    ordering = ('-created_at',)  # Order by most recent creation date

@admin.register(EmergencyCare)
class EmergencyCareAdmin(admin.ModelAdmin):
     list_display = ('patient_name', 'contact_number', 'condition_description', 'priority_level')
     search_fields = ('patient_name', 'contact_number', 'condition_description', 'priority_level', )
     list_filter = ('patient_name','condition_description', 'priority_level',)
        # Order by most recent creation date

