from django.db import models


# Create your models here.
class Rate(models.Model):
    buy = models.DecimalField(max_digits=6, decimal_places=2)
    sell = models.DecimalField(max_digits=6, decimal_places=2)
    created = models.DateTimeField(null=True, blank=True)
    type = models.CharField(max_length=3)  # noqa:A003
    source = models.CharField(max_length=255)


class ContactUs(models.Model):
    email_from = models.EmailField(max_length=254)
    subject = models.CharField(max_length=254)
    message = models.CharField(max_length=254)
