# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect, reverse

# Create your views here.
def index(request):
    response = "Welcome to SOS"
    return HttpResponse(response)
