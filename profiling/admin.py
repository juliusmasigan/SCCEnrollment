from django.contrib import admin
from .models import PersonalInformation, Profile, ExtendedProfile

# Register your models here.

class PersonalInformationAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'gender', 'contact_number')

admin.site.register(PersonalInformation, PersonalInformationAdmin)


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('personal_info', 'school_last_attended', 'school_date_attended', 'active')
    
admin.site.register(Profile, ProfileAdmin)


class ExtendedProfileAdmin(admin.ModelAdmin):
    list_display = ('profile', )

admin.site.register(ExtendedProfile, ExtendedProfileAdmin)
