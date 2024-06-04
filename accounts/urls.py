
from django.contrib import admin
from django.urls import path, include
from .views import *
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    
    path('users/', UserView.as_view(), name='users'),
    path('signup/', RegisterUserView.as_view(), name='signup'),
    path('signin/', LoginUserView.as_view(), name='signin'),
    path('refresh/',TokenRefreshView.as_view(), name='refresh-token')
    
]
