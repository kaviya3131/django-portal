"""first_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from first_app import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('',views.index,name = 'index'),
    path('admin/', admin.site.urls),
    path('first_app/',include('first_app.urls')),
    path('signup/',views.signup,name='signup'),
    path('postsignup/',views.postsignup,name='postsignup'),
    path('logout/',views.logout,name='logout'),
    path('classes/',views.classes,name='classes'),
    path('timetable/',views.timetable,name='timetable'),
    path('posttimetable/',views.posttimetable,name='posttimetable'),
    path('students/',views.students,name='students'),
    path('attendance/',views.attendance,name='attendance'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('addclass/',views.addclass,name='addclass'),
    path('editstudent/',views.editstudent,name='editstudent'),
    path('addstudents/',views.addstudents,name='addstudents'),
    path('post_addclass/',views.post_addclass,name='post_addclass'),
    path('post_index/',views.post_index,name='post_index'),
    
]

urlpatterns +=staticfiles_urlpatterns()