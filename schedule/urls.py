from django.urls import path, include
from .views import ScheduleListAPIView

urlpatterns = [
    path('schedule/', ScheduleListAPIView.as_view(), name='schedule-list'),

]
