from django.db import models


class Client(models.Model):
    firstname = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    house_number = models.IntegerField(null=True, blank=True)
    house_name = models.CharField(max_length=255, null=True, blank=True)
    address1 = models.CharField(max_length=255, null=True, blank=True)
    address2 = models.CharField(max_length=255, null=True, blank=True)
    address3 = models.CharField(max_length=255, null=True, blank=True)
    town = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    postcode = models.CharField(max_length=10, null=True, blank=True)
    telephone_number = models.CharField(max_length=20, null=True, blank=True)
    mobile_number = models.CharField(max_length=11, null=True, blank=True)
    email_address = models.EmailField(null=True, blank=True)

    def __str__(self):
        return "{} {}".format(self.firstname, self.surname)

    def get_mobile_number(self):
        return self.mobile_number[1:]
