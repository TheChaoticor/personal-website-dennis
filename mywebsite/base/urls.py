from django.urls import path
from . import views


urlpatterns = [
	path('', views.home),
    path('team/',views.team),
    path('project/',views.project),
    path('calender/',views.calender),
    path('basss/',views.basss),
    
]