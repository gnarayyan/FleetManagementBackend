from django.contrib import admin
from .models import CollectionPoint, CollectionRoute, Schedule, UserViewedSchedule
# Register your models here.
admin.site.register(CollectionPoint)
admin.site.register(CollectionRoute)
admin.site.register(Schedule)
admin.site.register(UserViewedSchedule)
