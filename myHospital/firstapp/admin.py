from django.contrib import admin
from .models import PhysicalAppointment

# Register your models here.
# admin.py
 

@admin.register(PhysicalAppointment)
class PhysicalAppointmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_no', 'service_needed', 'appointment_date', 'created_at')
    search_fields = ('name', 'email', 'phone_no', 'service_needed')
    list_filter = ('service_needed', 'appointment_date')
    ordering = ('-created_at',)  # Order by most recent creation date
