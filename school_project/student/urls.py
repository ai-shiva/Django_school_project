from django.urls import path
from student.views import StudentCreate ,StudentList ,StudentDetail ,StudentUpdate



urlpatterns = [
            path('admission/', StudentCreate.as_view()),
            path('list/', StudentList.as_view()),
            path('<pk>/',StudentDetail.as_view()),
            path('<pk>/edit',StudentUpdate.as_view()),


]












