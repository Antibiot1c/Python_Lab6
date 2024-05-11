from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('groups/', views.groups, name='groups'),
    path('students/', views.students, name='students'),
    path('group/<int:group_id>/', views.group_detail, name='group_detail'),
    path('student/<int:student_id>/', views.student_detail, name='student_detail'),
]
