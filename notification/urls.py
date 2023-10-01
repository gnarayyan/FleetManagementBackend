from django.urls import path
from . import views

urlpatterns = [
    path('', views.Device.as_view(
        {'get': 'list', 'post': 'create'}), name='device-list'),
    path('<int:pk>/', views.Device.as_view(
        {'get': 'retrieve', 'put': 'update', 'delete': 'destroy', 'patch': 'partial_update'}), name='device-detail'),

]
