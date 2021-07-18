from django.db import models
from staff.models import Staff
from parents.models import Parent
import datetime
from django.utils import timezone

class_choice = (('six','6th'),
				('seven','7th'),
				('eight','8th'),
				('nine','9th'),
				('ten','10th'),
				('eleven','11th'),
				('twelve','12th')
				)
gender_choice = (('m',"Male"),
				('f',"Female"))


class Student(models.Model):

	first_name = models.CharField(verbose_name="First Name",
									max_length=50,null=True)
	last_name = models.CharField(verbose_name="Last Name",
									max_length=50,null=True)
	age = models.PositiveSmallIntegerField(verbose_name="Age",default=0)

	gender = models.CharField(verbose_name="Gender", null=True,choices=gender_choice, max_length=50,default='m')

	student_class = models.CharField(choices=class_choice,
									verbose_name="Student Class",
									max_length=10,default = "six")
	mentor=models.ForeignKey(Staff,verbose_name="Mentor",on_delete = models.PROTECT)
	parent=models.ForeignKey(Parent,verbose_name="Parent",on_delete = models.PROTECT,null=True)
	
	dob = models.DateField(verbose_name="D.O.B")
	
	date_of_joined = models.DateField(auto_now_add=True)
	#date_of_joined = models.DateField(verbose_name="Date of joined", default=timezone.now)
	def __str__(self):
		return self.first_name+" "+self.last_name

	def save(self,*args, **kwargs):
		interval=datetime.date.today()-self.dob
		age=interval.days//365
		self.age=age
		super().save( *args, **kwargs)

		
