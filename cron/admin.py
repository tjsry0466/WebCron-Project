from django.contrib import admin
from .models import Schedule


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    pass