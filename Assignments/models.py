from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings


# Create your models here.
class Assignments(models.Model):
	subject = models.CharField(max_length=40)
	topics = models.CharField(max_length=200)
	teacher = models.CharField(max_length=40)
	due_date = models.DateField(auto_now_add = False)
	author = models.ForeignKey(
		settings.AUTH_USER_MODEL,
		on_delete = models.CASCADE,
		)

	def __str__(self):
		return self.subject + " " + self.topics

