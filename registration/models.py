from __future__ import unicode_literals

from django.db import models
from profiling.models import PersonalInformation

# Create your models here.

class Registrant(models.Model):
    primary_info = models.ForeignKey(PersonalInformation, related_name="primary_infos")
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
