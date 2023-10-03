from django.urls import path
from . import views
urlpatterns = [
    path('schedule/', views.ScheduleListAPIView.as_view(), name='schedule-list'),

    path('collection-points/', views.CollectionPointViewSet.as_view(
        {'get': 'list', 'post': 'create'}), name='collectionpoint-list'),
    path('collection-points/<int:pk>/', views.CollectionPointViewSet.as_view(
        {'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='collectionpoint-detail'),
    path('collection-routes/', views.CollectionRouteViewSet.as_view(
        {'get': 'list', 'post': 'create'}), name='collectionroute-list'),
    path('collection-routes/<int:pk>/', views.CollectionRouteViewSet.as_view(
        {'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='collectionroute-detail'),

    # Schedule Fleet
    path('fleet/', views.ScheduleFleet.as_view(
         {'get': 'list', 'post': 'create'}), name='device-list'),
    path('fleet/<int:pk>/', views.ScheduleFleet.as_view(
        {'get': 'retrieve', 'put': 'update', 'delete': 'destroy', 'patch': 'partial_update'}), name='device-detail'),

]
