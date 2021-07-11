from django.db import models

class_choice = (('six','6th'),
                ('seven','7th'),
                ('eight','8th'),
                ('nine','9th'),
                ('ten','10th'),
                ('eleven','11th'),
                ('twelve','12th')
                )
class Student(models.Model):
    student_name = models.CharField(verbose_name="Student Name",
                                    max_length=50)
    age = models.PositiveSmallIntegerField(verbose_name="Age")



    student_class = models.CharField(choices=class_choice,
                                    verbose_name="Student Class")

