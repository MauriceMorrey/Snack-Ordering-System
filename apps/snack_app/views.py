# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from ..login_and_registration.models import Users
from .models import *
import hashlib

from django.shortcuts import render, HttpResponse, redirect, reverse

# Create your views here.
def index(request):
    current_user = Users.objects.get(id=request.session["login"])
    print current_user.group.all()
    context = {
        "buygroup": BuyGroup.objects.all(),
        "user": current_user
    }
    print current_user.user_groups_joined
    return render(request, "sos/index.html", context)

def new(request):
    if "login" not in request.session:
        redirect("/")
    return render(request, "sos/create.html")

def create(request):
    errors = BuyGroup.objects.validate(request.POST)
    if len(errors):
        for error in errors:
            messages.error(request, error)
        return redirect('sos/new')
    current_user = Users.objects.get(id=request.session["login"])
    name = request.POST['name']
    password = request.POST['password']
    new = BuyGroup.objects.create(name=name, password=password, admin=current_user)
    new.users.add(current_user)
    return redirect('/sos')

def join(request, id = "None"):
    current_user = Users.objects.get(id=request.session["login"])
    group_buy = BuyGroup.objects.all().filter(name=id)
    if "login" not in request.session:
        redirect("/")
    if request.method=="POST":
        if request.POST["password"] == group_buy[0].password:
            group_buy[0].users.add(current_user)
            return redirect('/')
        return render(request, "sos/join.html")
    else:
        if id is None:
            return redirect('/sos')
        else:
            if group_buy.count() < 1:
                messages.error(request, "No Group Named {}!".format(id))
                return redirect('/sos')
            # if current_user in group_buy[0].users:
            #     print "already a member"
            #     return redirect('/sos')
        context = {
            "group":group_buy[0].name
        }
        return render(request, "sos/join.html", context)

    return redirect('/sos')

def group(request, id):
    current_user = Users.objects.get(id=request.session["login"])
    group_buy = BuyGroup.objects.all().filter(id=id)
    if "login" not in request.session:
        redirect("/")
    if group_buy.count() < 1:
        messages.error(request, "No Group Named {}!".format(id))
        return redirect('/sos')
    if group_buy[0].admin == current_user:
        userlevel = "admin"
    elif BuyGroup.objects.all().filter(tas=current_user).count() > 0:
        userlevel = "ta"
    else:
        userlevel = "user"

    context = {
        "userlevel":userlevel,
        "group":group_buy[0]
    }
    return render(request, "sos/group.html", context)

def upgrade_user(request, user_id, group_id):
    current_user = Users.objects.get(id=request.session["login"])
    group_buy = BuyGroup.objects.all().filter(id=group_id)
    if "login" not in request.session:
        redirect("/")
    if current_user == group_buy[0].admin:
        group_buy[0].tas.add(Users.objects.get(id=user_id))
    return redirect('/sos')

def md5encode(key, group):
    return hashlib.sha256(key.encode()+group.encode()).hexdigest()
