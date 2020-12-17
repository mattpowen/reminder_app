from django.db import models


class message(models.Model):
    to_number = models.IntegerField()
    message_body = models.CharField(max_length=160)
    reminder_date = models.DateField()
    date_sent = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return "{}-{}".format(to_number, reminder_date)
