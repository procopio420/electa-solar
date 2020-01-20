from django.urls import path
from . import views
from services import views as sviews

urlpatterns = [
    path('', views.index, name='index'),
    path('service/<int:pk>', sviews.service, name='service')
]