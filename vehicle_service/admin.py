from django.contrib import admin
from .models import Component, Vehicle, Issue

@admin.register(Component)
class ComponentAdmin(admin.ModelAdmin):
    list_display = ('name', 'repair_price', 'purchase_price')

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('license_plate', 'model')

@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    list_display = ('vehicle', 'component', 'issue_type')
