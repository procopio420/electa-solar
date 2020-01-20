from django.urls import path
from . import views

urlpatterns = [
    path('service/<int:pk>/', views.service, name='service'),
]