from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Clientlogo)
class ClientlogoAdmin(admin.ModelAdmin):
    list_display = ('img',)

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('img','title','des')
