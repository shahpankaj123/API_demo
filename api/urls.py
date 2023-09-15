from django.contrib import admin
from django.urls import path,include
from api import views

urlpatterns = [
    path('studentlist/', views.studentlist.as_view()),
    path('studentcreate/', views.studentcreate.as_view()),
    path('studentretrive/<int:pk>', views.studentretrive.as_view()),
    path('studentupdate/<int:pk>', views.studentupdate.as_view()),
    path('studentdelete/<int:pk>', views.studentdelete.as_view()),
    path('studentlistcreate/', views.studentlistcreate.as_view()),
   
]