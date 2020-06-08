from django.shortcuts import render
from .models import Schedule
# Create your views here.

def ScheduleView(request):
	day = Schedule.objects.all()[0]
	routineB = "first period is programming"
	context ={
	'day':day,
	'routine':routineB,
	}

	return render(request,'schedule.html',context)