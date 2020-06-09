from django.db import models
from django.db.models import When
from django.urls import reverse
# Create your models here.
class Schedule(models.Model):
	DAY_CHOICES = [
	('A','A'),
	('B','B'),
	('C','C'),
	('D','D'),
	('E','E'),
	]
	day = models.CharField(max_length=1,choices=DAY_CHOICES)
	date = models.DateField(auto_now_add=True)

	def __str__(self):
		return self.day

class Routine(models.Model):
	DAY_CHOICES = [
	('A','A'),
	('B','B'),
	('C','C'),
	('D','D'),
	('E','E'),
	]
	day = models.CharField(max_length=1,choices=DAY_CHOICES)

	morning_lab = models.BooleanField(default = False)
	first_period = models.CharField(max_length=30, null = " ",blank=True,default = "-")
	second_period = models.CharField(max_length=30, null = " ",blank=True,default = "-")
	third_period = models.CharField(max_length=30, null = " ",blank=True,default = "-")

	after_morning_lab=models.BooleanField(default = False)	
	fourth_period = models.CharField(max_length=30, null = " ",blank=True,default = "-")
	fifth_period = models.CharField(max_length=30, null = " ",blank=True,default = "-")
	sixth_period = models.CharField(max_length=30, null = " ",blank=True,default = "-")

	afternoon_lab=models.BooleanField(default = False)
	seventh_period = models.CharField(max_length=30, null = " ",blank=True,default = "-")
	eigth_period = models.CharField(max_length=30, null = " ",blank=True,default = "-")
	ninth_period = models.CharField(max_length=30, null = " ",blank=True,default = "-")

	def __str__(self):
		return self.day + " Day Routine"



	
