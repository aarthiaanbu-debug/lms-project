from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import Course, Lesson, Enrollment, Progress, Payment


def home(request):
    courses = Course.objects.all()
    return render(request, "home.html", {"courses": courses})


def course_list(request):

    courses = Course.objects.all()

    return render(request, "course_list.html", {
        "courses": courses
    })


def course_detail(request, id):

    course = get_object_or_404(Course, id=id)

    # premium course check
    if course.is_premium:

        enrolled = Enrollment.objects.filter(
            user=request.user,
            course=course
        ).exists()

        if not enrolled:
            return render(request, "premium_lock.html", {
                "course": course
            })

    lessons = Lesson.objects.filter(course=course)

    return render(request, "course_detail.html", {
        "course": course,
        "lessons": lessons
    })


def enroll(request, course_id):

    course = get_object_or_404(Course, id=course_id)

    Enrollment.objects.get_or_create(
        user=request.user,
        course=course
    )

    return redirect('courses')


def lesson_video(request, id):

    lesson = get_object_or_404(Lesson, id=id)

    return render(request, "lesson.html", {
        "lesson": lesson
    })


from django.shortcuts import get_object_or_404, redirect
from .models import Lesson, Progress
from notifications.models import Notification

def complete_lesson(request, lesson_id):

    lesson = get_object_or_404(Lesson, id=lesson_id)

    Progress.objects.create(
        user=request.user,
        course=lesson.course
    )

    # Notification create
    Notification.objects.create(
        message=f"{request.user.username} completed a lesson in {lesson.course.title}"
    )

    return redirect('dashboard')

from notifications.models import Notification
from django.contrib.auth.models import User
from .models import Course, Lesson, Enrollment, Progress

def dashboard(request):

    total_users = User.objects.count()
    total_courses = Course.objects.count()
    total_lessons = Lesson.objects.count()
    total_enrollments = Enrollment.objects.count()

    completed_lessons = Progress.objects.count()

    notifications = Notification.objects.all().order_by('-id')[:5]

    context = {
        "total_users": total_users,
        "total_courses": total_courses,
        "total_lessons": total_lessons,
        "total_enrollments": total_enrollments,
        "completed_lessons": completed_lessons,
        "notifications": notifications
    }

    return render(request, "dashboard.html", context)