from django.db import models
from utils.file_rename import File
from django.contrib.auth.models import User

# Create your models here.


class Feedback(models.Model):
    description = models.CharField(max_length=300)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now=True)


class Waste(models.Model):
    # models.DecimalField(max_digits=30, decimal_places=20)
    latitude = models.CharField(max_length=256, default="")
    # models.DecimalField(max_digits=30, decimal_places=20)
    longitude = models.CharField(max_length=256, default="")
    waste_volume = models.DecimalField(max_digits=9, decimal_places=6)
    waste_nature = models.SmallIntegerField(
        choices=((1, 'Organic'), (2, 'Plastic'), (3, 'Glass'), (4, 'Debris')), default=1)
    image = models.ImageField(upload_to=File(
        'waste/').rename, null=True, blank=True)
    waste_for = models.SmallIntegerField(
        choices=((0, 'On Demand Waste'), (1, 'Waste for Money')), default=0)
    collection_status = models.SmallIntegerField(
        choices=((0, 'Collected'), (1, 'Remain to Collect')), default=1)

    def __str__(self) -> str:
        waste_for = 'On Demand Waste🎇' if self.waste_for == 0 else 'Waste for Money💰'
        return waste_for
