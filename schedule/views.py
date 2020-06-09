from django.shortcuts import render
from .models import Schedule,Routine
# Create your views here.

def ScheduleView(request):
	day = Schedule.objects.all()[0]
	context = {
		"day":day,
	}

	#finding which day is present day and showing the routine according to that
	routine = get_routine(str(day))
	context["routine"] = routine

	#finding all the remaining day schedule excluding the present day
	remaining_routine = Routine.objects.exclude(day=day)
	context["remaining_routine"] = remaining_routine

	return render(request,'schedule.html',context)

def get_routine(day):
	if str(day) == "A":
		routine=Routine.objects.get(day="A")
	elif str(day) == "B":
		routine=Routine.objects.get(day="B")
	elif str(day) == "C":
		routine=Routine.objects.get(day="C")
	elif str(day) == "D":
		routine=Routine.objects.get(day="D")
	elif str(day) == "E":
		routine=Routine.objects.get(day="E")
	return routine

