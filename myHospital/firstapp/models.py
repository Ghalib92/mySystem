from django.db import models

# Create your models here.
class PhysicalAppointment(models.Model):
    SERVICE_CHOICES = [
        ('Dentist', 'Dentist'),
        ('Surgery', 'Surgery'),
        ('Consultation', 'Consultation'),
    ]

    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_no = models.CharField(max_length=15)
    service_needed = models.CharField(max_length=50, choices=SERVICE_CHOICES)
    appointment_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.service_needed} on {self.appointment_date}"