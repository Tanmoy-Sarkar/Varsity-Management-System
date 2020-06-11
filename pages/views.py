from django.shortcuts import render
from schedule.models import Routine,Schedule
from schedule.views import get_routine
from academicnotice.models import AcademicNotice
from ClassNotice.models import ClassNotice
from Assignments.models import Assignments
# Create your views here.

def HomePageView(request):
	day = Schedule.objects.all()[0]
	context = {
		"day":day,
	}
	routine = get_routine(str(day))
	context["routine"] = routine

	academic_notices = AcademicNotice.objects.all()
	context["academic_notices"] = academic_notices

	class_notices = ClassNotice.objects.all()
	context["class_notices"] = class_notices

	assignments = Assignments.objects.all()[:4]
	context["assignments"] = assignments

	return render(request,'home.html',context)




