from django.db import models


class Slot(models.Model):
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
            super(Slot, self).save(*args, **kwargs)


class Appointment(models.Model):
    client = models.ForeignKey("client.Client", on_delete=models.CASCADE)
    appointment_slot = models.ForeignKey(Slot, on_delete=models.RESTRICT)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return "{} - {}".format(self.client, self.appointment_slot)

    def save(self):
        if Appointment.objects.filter(appointment_slot=self.appointment_slot).exists():
            print("Slot already exists")
        else:
            super(Appointment, self).save(*args, **kwargs)


class AppointmentReminders(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    reminder_date = models.DateField()
    reminder_sent = models.DateTimeField()

    def __str__(self):
        return "{} {}".format(self.appointment, self.reminder_date)