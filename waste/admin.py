from django.contrib import admin
from .models import Waste, Feedback
# Register your models here.


# admin.site.register(Waste)
admin.site.register(Feedback)


@admin.register(Waste)
class WasteAdmin(admin.ModelAdmin):
    list_display = ('id', 'latitude', 'longitude', 'waste_volume',
                    'waste_nature', 'waste_for', 'collection_status')
    list_filter = ('waste_nature', 'waste_for', 'collection_status')
    search_fields = ('latitude', 'longitude', 'waste_volume')
    list_per_page = 20
