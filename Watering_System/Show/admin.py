from django.contrib import admin
from .models import Manager_User

@admin.register(Manager_User)
class Manager_admin(admin.ModelAdmin):
    list_display = ('id', 'user', 'Household_Name', 'Area', 'Creat_day')
