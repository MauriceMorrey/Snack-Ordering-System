# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from ..login_and_registration.models import Users
from .models import *

from django.shortcuts import render, HttpResponse, redirect, reverse

# Create your views here.
def index(request):
    group = BuyGroup.objects.all()
    response = "Welcome to SOS"
    return HttpResponse(group)

def new(request):
    if "login" not in request.session:
        redirect("/")
    return render(request, "snack_app/create.html")
        
def create(request):
    errors = BuyGroup.objects.validate(request.POST)
    if len(errors):
        for error in errors:
            messages.error(request, error)
        return redirect('snack_app/new')
    current_user = Users.objects.get(id=request.session["login"])
    name = request.POST['name']
    password = request.POST['password']
    BuyGroup.objects.create(name=name, password=password, admin=current_user)
    return redirect('/snack_app')

def join(request, id = "None"):
    if "login" not in request.session:
        redirect("/")
    if id is not None:
        return render(request, "snack_app/join.html")
    else:
        return redirect('/snack_app')
    pass