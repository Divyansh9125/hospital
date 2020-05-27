from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeView, name='recp-home'),
    path('dash', views.dashboardView, name='recp-dash'),
    path('add-app', views.addAppointmentView, name='add-app'),
    path('upd-app', views.updateAppointmentView, name='upd-app'),
    path('upd-app-form/<int:pk>/', views.updateAppointmentFormView, name='upd-app-form'),
    path('del-app', views.deleteAppointmentView, name='del-app'),
]