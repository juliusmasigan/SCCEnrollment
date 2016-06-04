import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers

from profiling.models import Profile
from .models import MedicalHistory, Condition, Medication, Doctor, EmergencyCare, PreliminaryCare


@csrf_exempt
def get_medical_history(request, pk=None):
    response = HttpResponse()

    medical_history = MedicalHistory.objects.select_related().get(pk=pk)
    response.status_code = 200
    response.content = serializers.serialize('json', [medical_history, ], indent=2, use_natural_foreign_keys=True)
    return response


def create_medical_condition(data):
    conditions = []
    for datum in data:
        conditions.append(
            Condition.objects.create(name=datum.get('name'), description=datum.get('description'))
        )

    return conditions


def create_medical_medication(data):
    medications = []
    for datum in data:
        medications.append(
            Medication.objects.create(description=datum.get('description'))
        )

    return medications


def create_medical_familyDoctor(data):
    familyDoctors = []
    for datum in data:
        familyDoctors.append(
            Doctor.objects.create(
                name = datum.get('name'),
                address = datum.get('address'),
                contact_number = datum.get('contactNumber')
            )
        )

    return familyDoctors


@csrf_exempt
def set_medical_history(request):
    response = HttpResponse()
    data = json.loads(request.body)

    profile = Profile.objects.get(pk=data.get('profileID'))
    medical_history = MedicalHistory()
    medical_history.profile = profile
    medical_history.save()

    if data.get('conditions'):
        conditions = create_medical_condition(data.get('conditions'))
        for condition in conditions:
            medical_history.conditions.add(condition)

    if data.get('medications'):
       medications = create_medical_medication(data.get('medications'))
       for medication in medications:
           medical_history.medications.add(medication)

    if data.get('familyDoctors'):
       familyDoctors = create_medical_familyDoctor(data.get('familyDoctors'))
       for familyDoctor in familyDoctors:
           medical_history.family_doctors.add(familyDoctor)

    response.status_code = 200
    response.content = serializers.serialize('json', [medical_history,], use_natural_foreign_keys=True, indent=2)
    return response
