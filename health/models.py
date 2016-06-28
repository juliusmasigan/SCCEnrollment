from django.db import models
from profiling.models import Profile


class Condition(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return "%s" % (self.name, )

    def natural_key(self):
        return {
            'name': self.name,
            'description': self.description,
        }


class Medication(models.Model):
    description = models.TextField()

    def natural_key(self):
        return {
            'description': self.description,
        }


class Doctor(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=500, null=True, blank=True)
    contact_number = models.CharField(max_length=50, null=True, blank=True)

    def __unicode__(self):
        return "%s" % (self.name, )

    def natural_key(self):
        return {
            'name': self.name,
            'address': self.address,
            'contact_number': self.contact_number,
        }


class MedicalHistory(models.Model):
    profile = models.ForeignKey(Profile, related_name="medical_profiles")
    conditions = models.ManyToManyField(Condition, related_name="conditions", blank=True)
    medications = models.ManyToManyField(Medication, related_name="medications", blank=True)
    family_doctors = models.ManyToManyField(Doctor, related_name="doctors", blank=True)

    class Meta:
        verbose_name_plural = "Medical Histories"


class EmergencyCare(models.Model):
    profile = models.ForeignKey(Profile, related_name="emergency_profiles")
    protocol = models.TextField()


class PreliminaryCare(models.Model):
    profile = models.ForeignKey(Profile, related_name="preliminary_care_profiles")
    protocol = models.TextField()


class FoodPermission(models.Model):
    profile = models.ForeignKey(Profile, related_name="food_permission_profiles")
    protocol = models.TextField()
