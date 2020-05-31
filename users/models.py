from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class CustomUser(AbstractUser):
	roll = models.IntegerField(validators=[MinValueValidator(1604001),MaxValueValidator(1604060)],null=True,blank=False)
	email = models.EmailField(null=False,blank=False)
	REQUIRED_FIELDS = ['roll','email']