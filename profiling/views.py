import json, datetime, re

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.db.models import Q

from profiling.models import PersonalInformation, Profile, ExtendedProfile, School


@csrf_exempt
def list_personal_information(request):
    response = HttpResponse()
    last_id = request.GET.get('lastID') or 0

    students = PersonalInformation.objects.filter(pk__gt=last_id)
    response.status_code = 200
    response.content = serializers.serialize('json', students)
    return response


@csrf_exempt
def get_personal_information(request, pk=None):
    response = HttpResponse()

    student = PersonalInformation.objects.get(pk=pk)
    response.status_code = 200
    response.content = serializers.serialize('json', [student,])
    return response
    
"""
Create new Personal Information record.

"""
@csrf_exempt
def set_personal_information(request):
    response = HttpResponse()
    data = json.loads(request.body)

    student = PersonalInformation()
    student.first_name = data.get('firstName')
    student.middle_name = data.get('middleName')
    student.last_name = data.get('lastName')
    student.gender = data.get('gender')
    student.address = data.get('address')
    student.contact_number = data.get('contactNumber')
    student.birth_place = data.get('birthPlace')
    student.birth_date = datetime.datetime.strptime(data.get('birthDate'), '%Y-%m-%d')
    student.save()

    response.status_code = 200
    response.content = serializers.serialize('json', [student,])
    return response


@csrf_exempt
def get_profile(request, pk=None):
    response = HttpResponse()

    profile = Profile.objects.select_related().get(pk=pk)
    response.status_code = 200
    response.content = serializers.serialize('json', [profile,], indent=2, use_natural_foreign_keys=True)
    return response


"""
Create new Profile.
"""
@csrf_exempt
def set_profile(request):
    response = HttpResponse()
    data = json.loads(request.body)

    try:
        personal_information = PersonalInformation.objects.get(pk=data.get('personID'))
    except PersonalInformation.DoesNotExist:
        return HttpResponse(status=400)

    if data.get('schoolID') is None:
        school = School()
        school.name = data.get('schoolName')
        school.address = data.get('schoolAddress')
        school.save()
    else:
        school = School.objects.get(pk=data.get('schoolID'))

    profile = Profile()
    profile.personal_info = personal_information
    profile.birth_date = datetime.datetime.strptime(data.get('birthDate'), '%Y-%m-%d')
    profile.birth_place = data.get('birthPlace')
    profile.father_name = data.get('fatherName')
    profile.father_occupation = data.get('fatherOccupation')
    profile.father_contact_number = data.get('fatherContactNumber')
    profile.mother_name = data.get('motherName')
    profile.mother_occupation = data.get('motherOccupation')
    profile.mother_contact_number = data.get('motherContactNumber')
    profile.guardian_name = data.get('guardianName')
    profile.guardian_address = data.get('guardianAddress')
    profile.guardian_contact_number = data.get('guardianContactNumber')
    profile.school_last_attended = school
    profile.school_date_attended = data.get('schoolDateAttended')
    profile.save()
    
    response.status_code = 200
    response.content = serializers.serialize('json', [profile,], indent=2, use_natural_foreign_keys=True)
    return response


@csrf_exempt
def get_extended_profile(request, pk=None):
    response = HttpResponse()

    extended_profile = ExtendedProfile.objects.select_related().get(pk=pk)
    response.status_code = 200
    response.content = serializers.serialize('json', [extended_profile,], indent=2, use_natural_foreign_keys=True)
    return response


"""
Create new Extended Profile.
"""
@csrf_exempt
def set_extended_profile(request):
    response = HttpResponse()
    data = json.loads(request.body)

    try:
        profile = Profile.objects.get(pk=data.get('profileID'))
    except Profile.DoesNotExist:
        return HttpResponse(status=400)

    extended_profile = ExtendedProfile()
    extended_profile.profile = profile
    extended_profile.awards = data.get('awards')
    extended_profile.skills = data.get('skills')
    extended_profile.save()

    if data.get('siblingsID'):
        siblings = PersonalInformation.objects.filter(pk__in=data.get('siblingsID'))
        for sibling in siblings:
            extended_profile.sibling.add(sibling)

    response.status_code = 200
    response.content = serializers.serialize('json', [extended_profile,], use_natural_foreign_keys=True, indent=2)
    return response
