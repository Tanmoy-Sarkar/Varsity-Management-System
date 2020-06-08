from django.urls import path
from .views import ScheduleView

urlpatterns = [
	path('',ScheduleView,name='schedule'),
]
