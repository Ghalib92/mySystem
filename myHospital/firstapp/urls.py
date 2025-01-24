from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('online_consultations/', views.online, name='online_consultations'),
    path('physical_appointment/', views.physical, name='physical_appointment'),
    path('emergency_care/', views.emergency, name='emergency_care'),
    path('emergency_booked',views.emergency_booked, name='emergency_booked'),
    path('booking-success/<int:appointment_id>/', views.booking, name='booking_success'),

 ]