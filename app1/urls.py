
from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.login,name='login'),
    path('home',views.home,name='home'),
    path('about',views.about,name='about'),
    path('addstudent',views.addstudent,name='addstudent'),
    path('editstudents<int:id>',views.editstudents,name='editstudents'),
    path('updatestudents<int:id>',views.updatestudents,name='updatestudents'),
    path('deletestudents<int:id>',views.deletestudents,name='deletestudents'),
    path('studentsession',views.studentsession,name='studentsession'),
    path('logout',views.logout,name='logout'),
    path('row',views.row,name='body'),
    path('body',views.body,name='body'),
]
