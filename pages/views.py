from django.shortcuts import render
from schedule.models import Routine,Schedule
from schedule.views import get_routine
# Create your views here.

def HomePageView(request):
	day = Schedule.objects.all()[0]
	context = {
		"day":day,
	}
	routine = get_routine(str(day))
	context["routine"] = routine

	return render(request,'home.html',context)




