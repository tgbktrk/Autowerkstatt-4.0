from django.contrib import admin
from .models import Car

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ("vin_number","licence_plate","brand","model","year","color","owner","slug",)
    search_fields = ("vin_number", 'licence_plate', 'brand', 'model', 'owner')
    prepopulated_fields = {"slug": ("licence_plate",),}

    def measurement_count(self, obj):
        return obj.measurement_set.count()