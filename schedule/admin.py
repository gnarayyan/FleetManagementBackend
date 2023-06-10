from django.contrib import admin
from .models import CollectionPoint, CollectionRoute, Schedule
# Register your models here.
admin.site.register(CollectionPoint)
admin.site.register(CollectionRoute)
admin.site.register(Schedule)
