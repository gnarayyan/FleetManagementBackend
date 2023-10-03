from django.contrib import admin
from . import models


admin.site.register(models.CollectionPoint)
admin.site.register(models.CollectionRoute)
admin.site.register(models.Schedule)
admin.site.register(models.ScheduleFleet)
admin.site.register(models.UserViewedSchedule)
