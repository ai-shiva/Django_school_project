from django.db import models


relation_choice = (('father','Father'),
				('mother','Mother'),
				('guardian','Guardian'),)

class Parent(models.Model):
	name = models.CharField(verbose_name="Parent Name",max_length=50)
	relation = models.CharField(choices=relation_choice,
								verbose_name = "Student Relation",max_length=20)

	def __str__(self):
		return self.name
	