from rest_framework import viewsets
from . import models, serializers


class Device(viewsets.ModelViewSet):
    queryset = models.Device.objects.all()
    serializer_class = serializers.Device
