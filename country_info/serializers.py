from rest_framework import serializers
from . import models


class Municipality(serializers.ModelSerializer):
    class Meta:
        model = models.Municipality
        fields = ('id', 'name',)
