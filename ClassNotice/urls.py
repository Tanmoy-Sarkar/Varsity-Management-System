from django.urls import path

from .views import ClassNoticeView

urlpatterns = [
	path('',ClassNoticeView.as_view(),name='class_notice_list')
]