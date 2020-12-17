from django.contrib import admin
from .models import Appointment, Slot, AppointmentReminders

admin.site.register(Appointment)
admin.site.register(Slot)
admin.site.register(AppointmentReminders)
