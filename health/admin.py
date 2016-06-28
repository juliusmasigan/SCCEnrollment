from django.contrib import admin
from .models import MedicalHistory, Doctor, Condition, Medication, \
EmergencyCare, PreliminaryCare, FoodPermission


class MedicalHistoryAdmin(admin.ModelAdmin):
    list_display = ('profile', )

admin.site.register(MedicalHistory, MedicalHistoryAdmin)


class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'contact_number', )

admin.site.register(Doctor, DoctorAdmin)


class ConditionAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', )

admin.site.register(Condition, ConditionAdmin)


class MedicationAdmin(admin.ModelAdmin):
    list_display = ('description', )

admin.site.register(Medication, MedicationAdmin)


class EmergencyCareAdmin(admin.ModelAdmin):
    list_display = ('profile', )

admin.site.register(EmergencyCare, EmergencyCareAdmin)


class PreliminaryCareAdmin(admin.ModelAdmin):
    list_display = ('profile', )

admin.site.register(PreliminaryCare, PreliminaryCareAdmin)


class FoodPermissionAdmin(admin.ModelAdmin):
    list_display = ('profile', )

admin.site.register(FoodPermission, FoodPermissionAdmin)
