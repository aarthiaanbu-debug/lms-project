from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .models import Course, Enrollment
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages


def home(request):
    courses = Course.objects.all()
    return render(request, "home.html", {"courses": courses})



def student_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('/courses/')
    
    return render(request, "login.html")

def enroll_course(request, course_id):

    course = Course.objects.get(id=course_id)

    Enrollment.objects.get_or_create(
        user=request.user,
        course=course
    )

    return redirect('/courses/')