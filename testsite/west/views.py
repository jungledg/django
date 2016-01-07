# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render
from models import Character


# Create your views here.

def staff(request):
    staff_list = Character.objects.all()
    # staff_str = map(str, staff_list)
    # context = {'label': ' '.join(staff_str)}
    #return HttpResponse("<p>" + ' '.join(staff_str) + "</p>")
    return render(request, 'templay.html', {'staffs': staff_list})

def templay(request):
    context          = {}
    context['label'] = 'Hello World!'
    return render(request, 'templay.html', context)