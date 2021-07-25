from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from .models import Student
from django.shortcuts import render


def Home(request):
    return render(request, "home.html")

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
    
    success_url ="/list"


class StudentList(ListView):
 

    model = Student


class StudentDetail(DetailView):
 

    model = Student

class StudentUpdate(UpdateView):

    model = Student


    fields = [  'first_name',
                'last_name',
                'gender',
                'student_class',
                'mentor',
                'parent',
                'dob',
            ]

    success_url ="/list"







