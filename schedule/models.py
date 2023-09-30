from django.db import models
from django.contrib.auth.models import User
from country_info.models import Municipality
# Create your models here.


class CollectionRoute(models.Model):
    name = models.CharField(max_length=256)
    municipality = models.ForeignKey(Municipality, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.name


class CollectionPoint(models.Model):
    # models.DecimalField(max_digits=20, decimal_places=15)
    latitude = models.CharField(max_length=256, default="")
    # models.DecimalField(max_digits=20, decimal_places=15)
    longitude = models.CharField(max_length=256, default="")
    name = models.CharField(max_length=100)
    collection_route = models.ForeignKey(
        CollectionRoute, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.name


class Schedule(models.Model):
    title = models.CharField(max_length=256)
    description = models.CharField(max_length=256)
    schedule_for = models.DateTimeField()
    collection_route = models.ForeignKey(
        CollectionRoute, on_delete=models.PROTECT)
    related_actor = models.CharField(
        max_length=1, choices=[('D', 'Driver'), ('S', 'System')], default='D')
    schedule_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        from django.contrib.humanize.templatetags import humanize
        return self.title + ' ▶ ' + humanize.naturaltime(self.schedule_at)


class UserViewedSchedule(models.Model):
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    # status = models.SmallIntegerField(
    #     choices=[(0, 'Not Viewed'), (1, 'Viewed')], default=0)
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self) -> str:
        fullname = self.user.get_full_name()
        title = self.schedule.title

        return fullname + '   🟩' + title + '🟩'
