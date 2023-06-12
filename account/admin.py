from django.contrib import admin
from .models import UserProfileModel, DriverCollectionMode

# Register your models here.
# admin.site.register(UserRoleModel)
admin.site.register(UserProfileModel)
admin.site.register(DriverCollectionMode)
