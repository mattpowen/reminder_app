from django.db import models
from send_sms.models import message

import logging

logger = logging.getLogger(__name__)


class Slot(models.Model):
    day = models.DateField()
    start = models.TimeField()
    end = models.TimeField()
    blocked = models.BooleanField()

    def __str__(self):
        return "{} ({}-{})".format(self.day, self.start, self.end)

    def save(self, *args, **kwargs):
        if self.start > self.end:
            print("Start time shouldn't be after end time")
        else:
            super(Slot, self).save(*args, **kwargs)


class Appointment(models.Model):
    client = models.ForeignKey("client.Client", on_delete=models.CASCADE)
    appointment_slot = models.ForeignKey(Slot, on_delete=models.RESTRICT)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return "{} - {}".format(self.client, self.appointment_slot)

    def save(self, *args, **kwargs):
        if Appointment.objects.filter(appointment_slot=self.appointment_slot).exists():
            print("Slot already exists")
        else:
            super(Appointment, self).save(*args, **kwargs)


class AppointmentReminders(models.Model):
    TYPE = (("email", "Email"), ("sms", "SMS"), ("telephone", "Telephone"))
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    reminder_date = models.DateField()
    reminder_type = models.CharField(choices=TYPE, max_length=9)
    reminder_sent = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return "{} {}".format(self.appointment, self.reminder_date)

    def save(self, *args, **kwargs):

        if not self.id:
            if self.appointment.client.mobile_number:
                new_message = message(
                    to_number="44".format(self.appointment.client.mobile_number),
                    message_body="Hi {}, This is a reminder you have an appointment on {}".format(
                        self.appointment.client.firstname, self.reminder_date
                    ),
                    reminder_date=self.reminder_date,
                )
                new_message.save()
            else:
                logger.warning("Client has not provided a mobile number")
        return super(AppointmentReminders, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Appointment Reminders"
