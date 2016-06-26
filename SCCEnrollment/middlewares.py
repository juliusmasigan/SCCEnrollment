import re, json

from django.http import HttpResponse
from django.db.utils import IntegrityError


class JSONMiddleware(object):

    def is_valid_json(self, data):
        try:
            json.loads(data)
        except ValueError as e:
            return False

        return True

    def process_request(self, request):
        if request.method == "GET":
            return None

        # If request is from admin path, allow www-form-data.
        if re.match(r'^\/admin.*', request.path):
            return None

        content_type = request.META.get('CONTENT_TYPE')
        if re.match(r'^application\/json', content_type) is None:
            return HttpResponse(status=400)

        if not self.is_valid_json(request.body):
            return HttpResponse(status=400)

        return None

    def process_response(self, request, response):
        if not re.match(r'^\/admin.*', request.path):
            response['Content-Type'] = 'application/json'

        return response

    def process_exception(self, request, exception):
        if re.search(r'matching query does not exist', exception.message, re.I):
            return HttpResponse(status=404)

        if type(exception) == IntegrityError:
            return HttpResponse(status=400)

        if type(exception) == TypeError:
            return HttpResponse(status=400)
