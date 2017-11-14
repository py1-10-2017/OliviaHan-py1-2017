# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

import random

def index(request):

    try:
        request.session['gold']

    except KeyError:
        request.session['gold'] = 0

    try:
        request.session['activities']
    except KeyError:
        request.session['activities'] = []


    return render(request, 'gold/index.html')

def process(request):

    money = random.randint(10, 20)
    request.session['gold'] += money
    action = '{} gold earned from farm!'.format(money)
    request.session['activities'].append(action)
    print request.session['activities']

    return redirect ('/')

def reset(request):
    request.session.flush()
    return redirect ('/')






# Create your views here.
