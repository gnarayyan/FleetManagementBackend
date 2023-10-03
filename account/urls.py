from django.urls import path, include
from rest_framework import routers
from . import views

# For JWT Authentication
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'test/', views.TestImage)
router.register(r'profile/', views.UserProfile)

urlpatterns = [
    path('login/', views.LoginView.as_view()),
    path('logout/', views.LogoutView.as_view()),
    path('profile/<int:pk>/',
         views.UserProfile.as_view({'get': 'retrieve'}), name='user-profile-by-id'),
    path('register/', include(router.urls)),
    path('register/user/', views.SignupAPIView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user-profiles/',
         views.UserProfileForSchedule.as_view({'get': 'list'}), name='user-profile-list'),
    # path('user-profiles/', views.UserProfileForSchedule.as_view(),
    #      name='user-profile-list'),

]
