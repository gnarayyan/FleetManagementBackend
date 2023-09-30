from rest_framework import viewsets
from . import serializers
from .import models


class Municipality(viewsets.ModelViewSet):
    serializer_class = serializers.Municipality
    queryset = models.Municipality.objects.all()
