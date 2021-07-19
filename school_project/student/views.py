from django.views.generic.edit import CreateView
from .models import Student


class StudentCreate(CreateView):

    model = Student

    # template_name = 'student_form.html'

    fields = [  'first_name',
                'last_name',
                'gender',
                'student_class',
                'mentor',
                'parent',
                'dob',
            ]


# class StudentList(ListView):
 

#     model = Student










