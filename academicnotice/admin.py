from django.contrib import admin
from .models import AcademicNotice
# Register your models here.
class MyModelAdmin(admin.ModelAdmin):
	fields = ['title','body']
	def save_model(self,request,obj,form,change):
		obj.author = request.user
		super().save_model(request, obj, form, change)
admin.site.register(AcademicNotice,MyModelAdmin)