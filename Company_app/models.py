from django.db import models
from django.utils import timezone
# required Company Schema
# -- UUID (primary Key)
# -- Company name
# -- Company CEO
# -- Company address
# -- Inception date

class Company(models.Model):
    UUID = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    CEO = models.CharField(max_length=20)
    address = models.CharField(max_length=40)
    date_field = models.DateField(default=timezone.now)

    # changing display name in django-admin panel
    def __str__(self):
        return str(self.UUID)+str(" ")+str(self.name)
