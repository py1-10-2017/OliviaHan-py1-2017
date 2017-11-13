# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from datetime import datetime

def index(request):
    return render(request, 'new_app/index.html')

def add_word(request):
    # new_word = {}
    # for key, value in request.POST.iteritems():
    #     if key != 'csrfmiddlewaretoken' and key != 'show-big':
    #         new_word[key] = value
    #     if key == 'show-big':
    #         new_word['big'] = 'big'
    #     else:
    #         new_word['big'] = ''
    # new_word['created_at'] = datetime.now().strftime('%H:%M %p, %B %d, %Y')

    new_word = {}
    new_word['content'] = request.POST['content']
    new_word['color'] = request.POST['color']
    try:
         request.POST['show-big']
         new_word['big'] = 'big'
    except KeyError:
        new_word['big'] = ''

    new_word['created_at'] = datetime.now().strftime('%H:%M %p, %B %d, %Y')




    try:
        request.session['words']
    except KeyError:
        request.session['words'] = []

    temp_list = request.session['words']
    temp_list.append(new_word)
    request.session['words'] = temp_list


    # 
    # for key, val in request.session.__dict__.iteritems():
    #     print key,val
    # print "past created at", new_word

    return redirect('/')

def clear(request):
    for key in request.session.keys():
        del request.session[key]

    return redirect('/')


# Create your views here.
