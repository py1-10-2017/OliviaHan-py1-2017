# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request, 'survey_form/index.html')

def process(request):
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['loc']
    request.session['language'] = request.POST['language']
    request.session['comment'] = request.POST['comment']

    return redirect ('/result')

def result(request):
    return render(request, 'survey_form/result.html')

def back(request):
    return redirect('/')


# Create your views here.
