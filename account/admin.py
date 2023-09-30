from django.contrib import admin
from .models import UserProfileModel, DriverCollectionMode, TestImage

# Register your models here.
# admin.site.register(UserRoleModel)
admin.site.register(UserProfileModel)
admin.site.register(DriverCollectionMode)
admin.site.register(TestImage)
