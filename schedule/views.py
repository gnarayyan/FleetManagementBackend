from rest_framework import generics, viewsets, status
from rest_framework.response import Response

from . import models, serializers
from notification.models import Device as DeviceNotificationModel
from utils.push_notification import PushNotification

notification = PushNotification()


class CollectionPointViewSet(viewsets.ModelViewSet):
    queryset = models.CollectionPoint.objects.all()
    serializer_class = serializers.CollectionPointSerializer


class CollectionRouteViewSet(viewsets.ModelViewSet):
    queryset = models.CollectionRoute.objects.all()
    serializer_class = serializers.CollectionRouteSerializer


class ScheduleListAPIView(generics.ListAPIView):
    serializer_class = serializers.ScheduleSerializer

    def get_queryset(self):
        collection_route = self.request.query_params.get(
            'collection_route', None)
        if collection_route is not None:
            queryset = models.Schedule.objects.filter(
                collection_route=collection_route)
        else:
            queryset = models.Schedule.objects.all()

        return queryset.order_by('-schedule_at')


class ScheduleFleet(viewsets.ModelViewSet):
    queryset = models.ScheduleFleet.objects.all()
    serializer_class = serializers.ScheduleFleet

    def partial_update(self, request, pk=None):
        instance = self.get_object()
        status = request.data.get('status')
        status = int(status) if status is not None else False
        new_driver = request.data.get('driver')
        new_driver = int(new_driver) if new_driver is not None else False

        schedule = ScheduleFleet.objects.get(id=pk)
        image_url = None if schedule.image == None else schedule.image.url

        # If status=reject
        if status == 2:
            # send PN to admin
            admin_token = DeviceNotificationModel.objects.get(
                user__username='admin').token
            title = 'Driver rejected the Request'
            body = 'Please reschedule the work to another driver'
            notification.send(admin_token, title, body, image=image_url)

        # If status=accept
        elif status == 1:
            # send PN to admin
            admin_token = DeviceNotificationModel.objects.get(
                user__username='admin').token
            title = 'Driver accepted the Request'
            body = 'Now, all respective household users will be notified'
            notification.send(admin_token, title, body, image=image_url)

            # send PN to all household users of that collection route
            tokens = DeviceNotificationModel.objects.filter(
                user__userprofilemodel__collection_route=instance.collection_route).values_list('token', flat=True)
            notification.sendAtBulk(
                tokens=tokens, title=schedule.title, body=schedule.description, image=image_url)

        # if driver is changed by admin
        elif new_driver != instance.driver:
            # send push notification to new driver
            driver_token = DeviceNotificationModel.objects.get(
                user=int(new_driver)).token
            notification.send(driver_token, title=schedule.title,
                              body=schedule.description, image=image_url)

        # Perform the partial update using the serializer
        serializer = self.get_serializer(
            instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK)

    def create(self, request):
        title = self.request.data['title']
        body = self.request.data['description']
        image = self.request.data['image']
        driver = self.request.data['driver']

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()  # Save the object
        image_url = request.build_absolute_uri(instance.image.url)

        driver_token = DeviceNotificationModel.objects.get(
            user=int(driver)).token
        # print('Created schedule img url: ', f'{image_url}')
        #       f'{request.META["HTTP_HOST"]}{image_url}')
        notification.send(driver_token, title=title,
                          body=body, image=image_url)

        return Response(status=status.HTTP_201_CREATED)
