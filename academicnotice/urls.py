from django.urls import path
from .views import AcademicNoticeView
urlpatterns = [
	path('',AcademicNoticeView.as_view(),name='academic_notice',)
]