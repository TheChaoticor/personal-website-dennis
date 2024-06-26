from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='dashboard'),
    path('team/', views.team, name='team'),
    path('project/', views.project, name='project'),
    path('calendar/', views.calender, name='calender'),
]
