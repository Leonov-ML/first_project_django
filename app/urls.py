from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home_view'),
    path('', views.time_view, name='time_view'),
    path('', views.workdir_view, name='workdir_view'),
]