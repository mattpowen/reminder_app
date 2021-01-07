from django.db import models


class email_message(models.Model):
    subject = models.CharField(max_length=150)
    message = models.TextField()
    to_address = models.EmailField()

    reminder_date = models.DateField()
    date_sent = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return "{}-{}".format(self.to_address, self.reminder_date)