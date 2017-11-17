# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, 'index.html')

def dashboard(request):
    return render(request, "libreria/dashboard/index.html")