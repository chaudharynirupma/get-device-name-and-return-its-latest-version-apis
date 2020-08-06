
from django.urls import path,include
from . import views

urlpatterns = [
    path('save-info/', views.device_info),
    path('get-info/', views.get_device_info),


]