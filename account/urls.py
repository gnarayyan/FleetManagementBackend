from django.urls import path
from .views import  LoginAPIView
from .views import  UserSignupAPIView



urlpatterns = [
    path('login/', LoginAPIView.as_view()),
    path('signup/', UserSignupAPIView.as_view()),


]
