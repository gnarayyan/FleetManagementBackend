from rest_framework import generics, status
from rest_framework.response import Response
from .models import Schedule
from .serializers import ScheduleSerializer


class ScheduleListAPIView(generics.ListAPIView):
    serializer_class = ScheduleSerializer

    def get_queryset(self):
        collection_route = self.request.query_params.get(
            'collection_route', None)
        if collection_route is not None:
            queryset = Schedule.objects.filter(
                collection_route=collection_route)
        else:
            queryset = Schedule.objects.all()

        return queryset.order_by('-schedule_at')

    # def get_queryset(self):
    #     collection_route = self.request.query_params.get(
    #         'collection_route', None)
    #     if collection_route is not None:
    #         return Schedule.objects.filter(collection_route=collection_route)
    #     else:
    #         error_message = "Please provide a collection route to get notifications"
    #         return Response({"error": error_message}, status=status.HTTP_400_BAD_REQUEST)
