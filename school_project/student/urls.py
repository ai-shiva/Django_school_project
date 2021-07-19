from django.urls import path
from student.views import StudentCreate



urlpatterns = [

            path('admission/', StudentCreate.as_view()),
            # path('list/', StudentList.as_view())

]












