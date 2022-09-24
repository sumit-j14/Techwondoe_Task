from django.db import models
from Company_app.models import Company
#  Team Schema
# -- UUID (primary Key)
# -- CompanyID (Foreign Key)
# -- Team Lead Name

class Team(models.Model):
    UUID = models.IntegerField(primary_key=True)
    CompanyID = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='teams')
    Team_lead = models.CharField(max_length=20)

    # changing display name in django-admin panel
    def __str__(self):
        return str(self.UUID) + str(" ") + str(self.Team_lead)