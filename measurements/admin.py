from django.contrib import admin
from .models import Measurement

@admin.register(Measurement) #decorator aracılığıyla kullandık
class MeasurementAdmin(admin.ModelAdmin):
    list_display = ("date","csv_file", "slug",)
    list_display_links = ("date",)
    prepopulated_fields = {"slug": ("date",),}
    list_filter = ("date",)
    search_fields = ("date",)

    def car_list(self, obj):
        html = ""
        for car in obj.cars.all():
            html += car.vin_number + " "
        return html