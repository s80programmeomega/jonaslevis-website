from django.contrib.auth.models import User
from django.http import HttpRequest

def project_processor(request: HttpRequest):
    return {'current_user': User.objects.first()}