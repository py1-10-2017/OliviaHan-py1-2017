# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(request):
    try:
        request.session['number']
    except KeyError:
        request.session['number'] = 0
    return render(request,'generator/index.html')


def generate(request):

     request.session['number'] += 1
     request.session['generator'] = get_random_string(length = 14)

     return redirect ('/')

def reset(request):

    try:
        request.session['number']
        request.session['generator']
        del request.session['number']
        del request.session['generator']
    except KeyError:

        return redirect ('/')
    return redirect('/')








# Create your views here.
