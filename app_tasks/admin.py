from django.contrib import admin
from .models import Task, Status


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
	list_display = ['id', 'title']


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
	list_display = ['id', 'title', 'responsible', 'date_from', 'date_date_to', 'status']