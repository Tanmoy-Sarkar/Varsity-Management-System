from django.db import models
from django.urls import reverse
# Create your models here.
class Schedule(models.Model):
	DAY_CHOICES = [
	('A','A'),
	('B','B'),
	('C','C'),
	('D','D'),
	('F','F'),
	]
	day = models.CharField(max_length=1,choices=DAY_CHOICES)
	date = models.DateField(auto_now_add=True)


	def __str__(self):
		return self.day

	
	
