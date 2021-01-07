from django import forms
from .models import Appointment, AppointmentReminders

import datetime


class AppointmentForm(forms.ModelForm):
    send_reminder = forms.BooleanField()
    reminder_date = forms.IntegerField()
    reminder_type = forms.ChoiceField(
        widget=forms.RadioSelect, choices=AppointmentReminders.TYPE
    )

    class Meta:
        model = Appointment
        fields = ["client", "appointment_slot", "notes"]

    def save(self, commit=True):
        instance = super(AppointmentForm, self).save(commit=False)
        send_reminder = self.cleaned_data["send_reminder"]

        instance.save()

        if send_reminder:
            appointment_date = self.cleaned_data["appointment_slot"].day
            days = datetime.timedelta(self.cleaned_data["reminder_date"])
            reminder_date = appointment_date - days
            new_reminder = AppointmentReminders(
                appointment=instance,
                reminder_date=reminder_date,
                reminder_type=self.cleaned_data["reminder_type"],
            )
            new_reminder.save()
        return instance