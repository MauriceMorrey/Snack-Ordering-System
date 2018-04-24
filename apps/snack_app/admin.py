# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from . models import *#importing everything from the models file

# Register your models here.
admin.site.register(BuyGroup)#asking django to register a class on the admin site
admin.site.register(Items)
admin.site.register(Inventory)



# Register your models here.
