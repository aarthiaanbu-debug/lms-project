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
from django.shortcuts import render
from .models import Course, Lesson


def home(request):
    return render(request,"home.html")


def course_list(request):

    courses = Course.objects.all()

    return render(request,"course_list.html",{"courses":courses})


def course_detail(request,id):

    course = Course.objects.get(id=id)

    lessons = Lesson.objects.filter(course=course)

    return render(request,"course_detail.html",{
        "course":course,
        "lessons":lessons
    })
from django.shortcuts import redirect
from .models import Course, Enrollment

def enroll(request, course_id):

    course = Course.objects.get(id=course_id)

    Enrollment.objects.get_or_create(
        user=request.user,
        course=course
    )

    return redirect("course_detail", id=course_id)
    from .models import Course,Enrollment

def course_detail(request,id):

    course = Course.objects.get(id=id)

    if course.is_premium:

        enrolled = Enrollment.objects.filter(
            user=request.user,
            course=course
        ).exists()

        if not enrolled:
            return render(request,"premium_lock.html",{"course":course})

    lessons = course.lesson_set.all()

    return render(request,"course_detail.html",{
        "course":course,
        "lessons":lessons
    })
def complete_lesson(request,lesson_id):

    lesson = Lesson.objects.get(id=lesson_id)

    course = lesson.course

    total = Lesson.objects.filter(course=course).count()

    progress,created = Progress.objects.get_or_create(
        user=request.user,
        course=course
    )

    progress.completed_lessons += 1

    progress.percent = int(
        (progress.completed_lessons/total)*100
    )

    progress.save()

    return redirect("lesson",lesson_id=lesson_id)