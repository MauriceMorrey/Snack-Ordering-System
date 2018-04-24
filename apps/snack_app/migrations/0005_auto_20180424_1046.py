# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-24 02:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login_and_registration', '0001_initial'),
        ('snack_app', '0004_merge_20180424_1044'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buygroup',
            name='tas',
        ),
        migrations.RemoveField(
            model_name='buygroup',
            name='users',
        ),
        migrations.AddField(
            model_name='buygroup',
            name='ta',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ta_group', to='login_and_registration.Users'),
        ),
        migrations.AddField(
            model_name='buygroup',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_group', to='login_and_registration.Users'),
        ),
    ]
