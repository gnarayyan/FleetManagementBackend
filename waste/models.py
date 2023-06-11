from django.db import models
from account.models_helper import get_img_path

# Create your models here.


class Waste(models.Model):
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    waste_volume = models.DecimalField(max_digits=9, decimal_places=6)
    waste_nature = models.SmallIntegerField(
        choices=((1, 'Organic'), (2, 'Plastic'), (3, 'Glass'), (4, 'Debris')), default=1)
    image = models.ImageField(upload_to=get_img_path, null=True, blank=True)
    waste_for = models.SmallIntegerField(
        choices=((0, 'On Demand Waste'), (1, 'Waste for Money')), default=0)

    def __str__(self) -> str:
        return self.waste_for
