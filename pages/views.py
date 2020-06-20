from django.shortcuts import render
from schedule.models import Routine,Schedule
from schedule.views import get_routine
from academicnotice.models import AcademicNotice
from ClassNotice.models import ClassNotice
from Assignments.models import Assignments
# Create your views here.

def HomePageView(request):

	#current day
	day = Schedule.objects.all()[0]
	context = {
		"day":day,
	}

	#current routine of the day
	routine = get_routine(str(day))
	context["routine"] = routine

	#academic notices
	academic_notices = AcademicNotice.objects.all()
	context["academic_notices"] = academic_notices

	#class notices
	class_notices = ClassNotice.objects.all()
	context["class_notices"] = class_notices

	#assignments
	assignments = Assignments.objects.all()[:4]
	context["assignments"] = assignments

	return render(request,'home.html',context)




