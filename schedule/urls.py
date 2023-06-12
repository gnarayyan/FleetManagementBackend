from django.urls import path, include
from .views import ScheduleListAPIView, CollectionPointViewSet, CollectionRouteViewSet

urlpatterns = [
    path('schedule/', ScheduleListAPIView.as_view(), name='schedule-list'),

    path('collection-points/', CollectionPointViewSet.as_view(
        {'get': 'list', 'post': 'create'}), name='collectionpoint-list'),
    path('collection-points/<int:pk>/', CollectionPointViewSet.as_view(
        {'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='collectionpoint-detail'),
    path('collection-routes/', CollectionRouteViewSet.as_view(
        {'get': 'list', 'post': 'create'}), name='collectionroute-list'),
    path('collection-routes/<int:pk>/', CollectionRouteViewSet.as_view(
        {'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='collectionroute-detail'),
]
