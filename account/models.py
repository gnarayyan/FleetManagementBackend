from django.db import models
from django.contrib.auth.models import User
from country_info.models import Municipality
from schedule.models import CollectionRoute
from .models_helper import get_file_path


class UserProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to=get_file_path, null=True, blank=True)
    role =  models.CharField(max_length=1, choices = [('A', 'Admin'),('D','Driver'), ('H','Household User')], default='H')
    verification_status =  models.CharField(max_length=1, choices = [('V', 'Verified'),('U','Unverified')], default='U')
    municipality = models.ForeignKey(Municipality, on_delete=models.PROTECT, null=True)
    collection_route = models.ForeignKey(CollectionRoute, on_delete=models.PROTECT, null=True)


    def __str__(self):
        verify_status = '✔' if self.verification_status=='V' else '❌'
        return self.user.username + ' - ' + verify_status



class DriverCollectionMode(models.Model):
    collection_mode =  models.SmallIntegerField(
        choices=((0, 'OFF'), (1, 'ON')), default=0) 
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True)

    def __str__(self):
        collection_mode = '✔' if self.collection_mode==1 else '❌'
        return self.user.username + ' ▶ ' + collection_mode
