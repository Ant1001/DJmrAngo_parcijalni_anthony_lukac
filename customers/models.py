from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=255)
    vat_id = models.CharField(max_length=20, unique=True)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100, default='Hrvatska')

    def __str__(self):
        return self.name