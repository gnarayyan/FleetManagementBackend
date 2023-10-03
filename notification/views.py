from rest_framework import viewsets, generics
from . import models, serializers


class Device(viewsets.ModelViewSet):
    queryset = models.Device.objects.all()
    serializer_class = serializers.Device


class GetDeviceByUser(generics.RetrieveAPIView):
    queryset = models.Device.objects.all()
    serializer_class = serializers.Device
    lookup_field = 'user'
