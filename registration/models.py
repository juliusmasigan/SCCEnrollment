from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Schools(models.Model):
	name = models.CharField(max_length=255)
	address = models.CharField(max_length=500, blank=True)

class Registrant(models.Model):
	genders= (
		('male', 'Male'), 
		('female', 'Female'),
	)

	first_name = models.CharField(max_length=255)
	middle_name = models.CharField(max_length=255, blank=True)
	last_name = models.CharField(max_length=255, db_index=True)
	gender = models.CharField(max_length=6, choices=genders, default='male')
	address = models.CharField(max_length=500)
	contact_number = models.CharField(max_length=50, blank=True)

	class Meta:
		db_table = 'enrollment_registrant'

class Profile(models.Model):
	birth_date = models.DateField('Date of Birth')
	birth_place = models.CharField(max_length=500)
	# Father Info
	father_name = models.CharField(max_length=255)
	father_occupation = models.CharField(max_length=255, blank=True)
	father_contact_number = models.CharField(max_length=50, blank=True)
	# Mother Info
	mother_name = models.CharField(max_length=255)
	mother_occupation = models.CharField(max_length=255, blank=True)
	mother_contact_number = models.CharField(max_length=50, blank=True)
	# Guardian Info
	guardian_name = models.CharField(max_length=255, blank=True)
	guardian_contact_number = models.CharField(max_length=255, blank=True)
	guardian_address = models.CharField(max_length=500, blank=True)
	# Last Attended School Info
	school_last_attended = models.ForeignKey(Schools, related_name='school_last_attended')
	school_date_attended = models.DateField('Last Date Attended')
