from django.contrib import admin
from django.urls import path
from .views import MyTokenObtainPairView
# from base import views
from . import views
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.index),
    path('login/', views.MyTokenObtainPairView.as_view()), 

]
