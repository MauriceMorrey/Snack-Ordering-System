# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ..login_and_registration.models import Users
from .models import *

from django.shortcuts import render, HttpResponse, redirect, reverse

# Create your views here.
def index(request):
    response = "Welcome to SOS"
    return HttpResponse(response)

def creat_or_join(request, id = None):
    if "login" not in request.session:
        redirect("/")
    if id:
        current_user = Users.objects.get(id=request.session["login"])
        


