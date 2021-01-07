from django.contrib import admin
from .forms import AppointmentForm
from .models import Appointment, Slot, AppointmentReminders


class AppointmentAdmin(admin.ModelAdmin):
    form = AppointmentForm


admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(Slot)
admin.site.register(AppointmentReminders)
