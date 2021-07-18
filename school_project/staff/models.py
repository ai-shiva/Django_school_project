from django.db import models
import datetime
from django.utils import timezone


experience_choices = (
	("1", "1"),
	("2", "2"),
	("3", "3"),
	("4", "4"),
	("5", "5"),
	("more_than_5","More than 5")
)



class Staff(models.Model):
	name = models.CharField(verbose_name="Staff Name",
									max_length=50)
	experience = models.CharField(max_length = 20,
								choices = experience_choices,
								default = "1",
								verbose_name="Experience in years")
	date_of_joined = models.DateField(auto_now_add=True)
	#date_of_joined = models.DateField(default=timezone.now)
	
	def __str__(self):
		return self.name