from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeView, name='pat-home'),
    path('pat-prof', views.ProfileView, name='patient-profile'),
    path('pat-app', views.AppointmentView, name='patient-appointment'),
]