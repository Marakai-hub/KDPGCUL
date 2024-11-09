from django.contrib import admin
from .models import Farmer, Query, Harvest, PlantingReport
from django.utils.crypto import get_random_string

# Farmer Admin
class FarmerAdmin(admin.ModelAdmin):
    list_display = ('farmer_id', 'name', 'sex', 'age', 'land_size', 'county', 'subcounty', 'parish', 'village')
    list_filter = ('sex', 'county', 'subcounty', 'parish', 'village')
    search_fields = ('farmer_id', 'name', 'county', 'subcounty', 'parish', 'village')
    ordering = ('name',)
    list_editable = ('age', 'land_size')
    fields = ('farmer_id', 'name', 'sex', 'age', 'land_size', 'county', 'subcounty', 'parish', 'village')

admin.site.register(Farmer, FarmerAdmin)

# Query Admin
class QueryAdmin(admin.ModelAdmin):
    list_display = ('farmer', 'issue', 'date_created')
    list_filter = ('date_created', 'farmer__county', 'farmer__subcounty')
    search_fields = ('farmer__name', 'issue')
    ordering = ('-date_created',)
    fields = ('farmer', 'issue', 'date_created')

admin.site.register(Query, QueryAdmin)

# Harvest Admin
class HarvestAdmin(admin.ModelAdmin):
    list_display = ('farmer', 'season', 'land_size', 'potato_kg', 'date_reported')
    list_filter = ('season', 'farmer__county', 'farmer__subcounty')
    search_fields = ('farmer__name', 'season')
    ordering = ('-date_reported',)
    fields = ('farmer', 'season', 'land_size', 'potato_kg', 'date_reported')

admin.site.register(Harvest, HarvestAdmin)

# PlantingReport Admin
class PlantingReportAdmin(admin.ModelAdmin):
    list_display = ('farmer', 'season', 'land_size', 'potato_kg', 'planting_date')
    list_filter = ('season', 'farmer__county', 'farmer__subcounty')
    search_fields = ('farmer__name', 'season')
    ordering = ('-planting_date',)
    fields = ('farmer', 'season', 'land_size', 'potato_kg', 'planting_date')

admin.site.register(PlantingReport, PlantingReportAdmin)

from django.contrib import admin
from .models import Event

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'location')
    list_filter = ('date',)
    search_fields = ('title', 'location')
    ordering = ('date',)

admin.site.register(Event, EventAdmin)
