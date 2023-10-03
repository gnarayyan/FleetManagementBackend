from django.contrib.humanize.templatetags import humanize
from rest_framework import serializers
from . import models


class CollectionPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CollectionPoint
        fields = '__all__'


class CollectionRouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CollectionRoute
        fields = '__all__'


class ScheduleSerializer(serializers.ModelSerializer):
    schedule_for = serializers.SerializerMethodField()
    schedule_at = serializers.SerializerMethodField()

    class Meta:
        model = models.Schedule
        fields = ['title', 'description', 'schedule_for',
                  'related_actor', 'schedule_at']

    def get_schedule_for(self, obj):
        return humanize.naturaltime(obj.schedule_for)

    def get_schedule_at(self, obj):
        return humanize.naturaltime(obj.schedule_at)
    # naturaltime(timezone.now() - obj.schedule_for)


class ScheduleFleet(serializers.ModelSerializer):
    class Meta:
        model = models.ScheduleFleet
        fields = ('id', 'title', 'description', 'image', 'accepted_at',
                  'status', 'collection_route', 'driver')
