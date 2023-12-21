from django.db import models

class Manager_User(models.Model):
    user = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    Household_Name = models.CharField(max_length=255)
    Area = models.CharField(max_length=255)
    Creat_day = models.DateField(auto_now_add=True)