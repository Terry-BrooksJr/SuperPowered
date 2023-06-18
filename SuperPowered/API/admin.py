from API.models import Alignment, Hero, Publisher, Race, SuperPower
from django.contrib import admin
from django.contrib.admin.models import LogEntry

all_models = [Race, Hero, Alignment, Publisher, SuperPower, LogEntry]
for model in all_models:
    try:
        if model != "TokenProxy":
            register = admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass
