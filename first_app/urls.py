from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('signup/',views.signup,name='signup'),
    path('postsignup/',views.postsignup,name='postsignup'),
    path('logout/',views.logout,name='logout'),
    path('classes/',views.classes,name='classes'),
    path('timetable/',views.timetable,name='timetable'),
    path('posttimetable/',views.posttimetable,name='posttimetable'),
    path('students/',views.students,name='students'),
    path('attendance/',views.attendance,name='attendance'),
    path('editstudent/',views.editstudent,name='editstudent'),
    path('addstudents/',views.addstudents,name='addstudents'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('addclass/',views.addclass,name='addclass'),
    path('post_addclass/',views.post_addclass,name='post_addclass'),
    path('post_index/',views.post_index,name='post_index'),

]