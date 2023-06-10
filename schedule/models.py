from django.db import models
from country_info.models import Municipality

# Create your models here.


class CollectionRoute(models.Model):
    name = models.CharField(max_length=256)
    municipality = models.ForeignKey(Municipality, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name


class CollectionPoint(models.Model):
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    municipality = models.ForeignKey(Municipality, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    collection_route = models.ForeignKey(
        CollectionRoute, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name


class Schedule(models.Model):
    title = models.CharField(max_length=256)
    description = models.CharField(max_length=256)
    schedule_for = models.DateTimeField()
    related_actor = models.CharField(
        max_length=1, choices=[('D', 'Driver'), ('S', 'System')], default='D')
    schedule_to = models.ForeignKey(CollectionRoute, on_delete=models.CASCADE)
    schedule_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
