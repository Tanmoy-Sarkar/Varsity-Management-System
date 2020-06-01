from django.views.generic import ListView
from .models import ClassNotice
# Create your views here.
class ClassNoticeView(ListView):
	model = ClassNotice
	template_name = 'class_notice_list.html'