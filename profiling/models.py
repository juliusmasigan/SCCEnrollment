from __future__ import unicode_literals

from django.db import models

# Create your models here.

class School(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=500, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def natural_key(self):
        return {'name':self.name, 'address':self.address}


class PersonalInformation(models.Model):
    genders= (
        ('male', 'Male'), 
        ('female', 'Female'),
    )

    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, db_index=True)
    gender = models.CharField(max_length=6, choices=genders, default='male')
    address = models.CharField(max_length=500)
    contact_number = models.CharField(max_length=50, null=True, blank=True)
    birth_date = models.DateField('Date of Birth')
    birth_place = models.CharField(max_length=500, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "%s, %s" % (self.last_name, self.first_name)

    def natural_key(self):
        return {
            'first_name':self.first_name,
            'middle_name':self.middle_name,
            'last_name':self.last_name,
            'gender':self.gender,
            'address':self.address,
            'birth_date':self.birth_date,
            'birth_place':self.birth_place,
        }


class Profile(models.Model):
    personal_info = models.ForeignKey(PersonalInformation, related_name="personal_infos")
# Father Info
    father_name = models.CharField(max_length=255, null=True, blank=True)
    father_occupation = models.CharField(max_length=255, null=True, blank=True)
    father_contact_number = models.CharField(max_length=50, null=True, blank=True)
# Mother Info
    mother_name = models.CharField(max_length=255, null=True, blank=True)
    mother_occupation = models.CharField(max_length=255, null=True, blank=True)
    mother_contact_number = models.CharField(max_length=50, null=True, blank=True)
# Guardian Info
    guardian_name = models.CharField(max_length=255, null=True, blank=True)
    guardian_contact_number = models.CharField(max_length=255, null=True, blank=True)
    guardian_address = models.CharField(max_length=500, null=True, blank=True)
# Last Attended School Info
    school_last_attended = models.ForeignKey(School, related_name='school_last_attended', null=True, blank=True)
    school_date_attended = models.DateField('Last Date Attended', null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=False)

    def __unicode__(self):
        return "%s, %s" % (self.personal_info.last_name, self.personal_info.first_name)


class ExtendedProfile(models.Model):
    profile = models.ForeignKey(Profile, related_name="extended_profiles")
    awards = models.TextField(null=True, blank=True)
    skills = models.TextField(null=True, blank=True)
    sibling = models.ManyToManyField(PersonalInformation, related_name="siblings")
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
