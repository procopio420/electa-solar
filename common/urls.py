from django.urls import path
from . import views
from services import views as sviews
from apps import views as aviews

urlpatterns = [
    path('', views.index, name='index'),
    path('service/<int:pk>', sviews.service, name='service'),
    path('email', views.send_email, name='email'),
    path('applications', aviews.apps, name='apps')
]