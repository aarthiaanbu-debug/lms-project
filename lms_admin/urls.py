from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('enroll/<int:course_id>/', views.enroll_course, name='enroll_course'),
]