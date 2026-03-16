from django.shortcuts import render, get_object_or_404, redirect
from models import Course, Lesson, Enrollment
from django.contrib.auth.decorators import login_required


# Course list
def course_list(request):

    courses = Course.objects.all()

    return render(request, 'learning/course.html', {
        'courses': courses
    })


# Course detail + lessons
def course_detail(request, id):

    course = get_object_or_404(Course, id=id)
    lessons = Lesson.objects.filter(course=course)

    return render(request, 'learning/course_detail.html', {
        'course': course,
        'lessons': lessons
    })


# Lesson video player
def lesson_video(request, id):

    lesson = get_object_or_404(Lesson, id=id)

    return render(request, 'learning/video_player.html', {
        'lesson': lesson
    })


# Enroll course
@login_required
def enroll(request, id):

    course = get_object_or_404(Course, id=id)

    Enrollment.objects.get_or_create(
        user=request.user,
        course=course
    )

    return redirect('dashboard')


# Student dashboard
@login_required
def dashboard(request):

    enrollments = Enrollment.objects.filter(user=request.user)

    return render(request, 'learning/dashboard.html', {
        'enrollments': enrollments
    })