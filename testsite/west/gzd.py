# -*- coding: utf-8 -*-

from django.http import HttpResponse

from models import Character


# Create your views here.

def gzd(request):
    return HttpResponse("<p>Hello World!</p>")
