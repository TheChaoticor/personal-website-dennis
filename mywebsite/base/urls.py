from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='dashboard'),
    path('team/', views.team, name='team'),
    path('project/', views.project, name='project'),
    path('calendar/', views.calender, name='calender'),
    path('team/', views.get_started, name='get_started'),
    path('contact/', views.contact, name='contact'),
    path('success/',views.success,name='success'),
    path('price/',views.price,name='price'),
    
]
