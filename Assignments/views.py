from django.views.generic import ListView
from .models import Assignments
# Create your views here.
class AssignmentView(ListView):
	model = Assignments
	template_name = 'assignment_list.html'

	