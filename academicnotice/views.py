from django.views.generic import ListView
from .models import AcademicNotice

# Create your views here.

class AcademicNoticeView(ListView):
	model = AcademicNotice
	template_name = 'academic_notice.html'
