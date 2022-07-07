from django.contrib import admin
from .models import Profile, Department


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
	list_display = ['id', 'user', 'phone', 'date_of_birth', 'department']

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
	list_display = ['id', 'name']