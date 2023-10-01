from rest_framework import serializers
from . import models


class Device(serializers.ModelSerializer):
    class Meta:
        model = models.Device
        fields = ('user', 'token', 'refresh_count', 'platform')
