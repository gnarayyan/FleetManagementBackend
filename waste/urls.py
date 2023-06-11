from django.urls import path, include
from rest_framework import routers
from .views import WasteViewSet

router = routers.DefaultRouter()
router.register(r'wastes', WasteViewSet)

urlpatterns = [
    path('demand/', include(router.urls)),
]
