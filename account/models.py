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

