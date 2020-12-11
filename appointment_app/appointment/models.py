from django.db import models


class Slots(models.Model):
    day = models.DateField()
    start = models.TimeField()
    end = models.TimeField()
    blocked = models.BooleanField()

    def __str__(self):
        return "{} ({}-{})".format(self.day, self.start, self.end)

    def save(self, *args, **kwargs):
        if self.start < self.end:
            print("Start time shouldn't be after end time")
        else:
            super(Slots, self).save(*args, **kwargs)


class Appointment(models.Model):
    client = models.ForeignKey("client.Client", on_delete=models.CASCADE)
    appointment_slot = models.ForeignKey(Slots, on_delete=models.RESTRICT)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return "{} - {}".format(client, appointment_slot)

    def save(self):
        if Appointment.objects.filter(appointment_slot=self.appointment_slot).exists():
            print("Slot already exists")
        else:
            super(Appointment, self).save(*args, **kwargs)


class AppointmentReminders(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    reminder = models.DateField()
    reminder_sent = models.DateTimeField()
