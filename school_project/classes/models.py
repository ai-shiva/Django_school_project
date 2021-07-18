from django.db import models


class Classes(models.Model):

	class_name=models.CharField(verbose_name="Class Name",unique=True,max_length=50)
	room_number=models.PositiveSmallIntegerField(verbose_name="Room Number",default=0)

	def __str__(self):
		return self.class_name