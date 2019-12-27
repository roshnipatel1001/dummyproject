from django.urls import path
from . import views

urlpatterns = [

    path('clg/', views.CollegeView.as_view()),
    path('clg/<int:pk>/', views.CollegeView.as_view()),
    path('student/', views.StudentView.as_view()),
    path('student/<int:pk>/', views.StudentView.as_view()),

]
