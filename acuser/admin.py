from django.contrib import admin

# Register your models here.
from .models import Names, Periods

admin.site.register(Names)

admin.site.register(Periods)