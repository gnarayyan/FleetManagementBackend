from django.contrib import admin
from . import models


@admin.register(models.Device)
class WasteAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'registered_on', 'platform',
                    'refresh_count', 'token')
    list_filter = ('platform',)
    search_fields = ('platform', 'user')
    list_per_page = 20
