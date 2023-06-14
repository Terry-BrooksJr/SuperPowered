from django.apps import apps
from django.contrib import admin
from django.contrib.admin.models import LogEntry
from icecream import ic
from API.models import Race, Hero, Alignment, Publisher, SuperPower
all_models = [Race, Hero, Alignment, Publisher, SuperPower, LogEntry ]
for model in all_models:
    try:
        if model != 'TokenProxy':
            register = admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass
