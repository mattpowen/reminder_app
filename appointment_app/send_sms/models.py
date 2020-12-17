from django.db import models


class message(models.Model):
    to_number = models.CharField(max_length=12)
    message_body = models.CharField(max_length=160)
    reminder_date = models.DateField()
    date_sent = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return "{}-{}".format(self.to_number, self.reminder_date)
