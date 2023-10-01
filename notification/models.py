from django.db import models
from account.models import User
# Create your models here.


class Device(models.Model):
    class Platforms(models.IntegerChoices):
        ANDROID = 0, 'Android'
        IOS = 1, 'IoS'
        WEB = 2, 'Web'
        WINDOWS = 3, 'Windows'
        MACOS = 4, 'MacOS'
        LINUX = 5, 'Linux'

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    registered_on = models.DateTimeField(auto_now=True)
    refresh_count = models.PositiveIntegerField(default=0)
    token = models.CharField(max_length=500)
    platform = models.PositiveSmallIntegerField(
        choices=Platforms.choices, default=Platforms.ANDROID)

    def save(self, *args, **kwargs):
        # Check if the token field has changed
        if self.pk is not None:
            original = Device.objects.get(pk=self.pk)
            if original.token != self.token:
                self.refresh_count += 1
        super(Device, self).save(*args, **kwargs)
