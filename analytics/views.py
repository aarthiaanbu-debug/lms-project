from django.shortcuts import render
from django.contrib.auth.models import User
from lms_admin.models import Course, Enrollment


def dashboard(request):

    total_users = User.objects.count()

    total_courses = Course.objects.count()

    total_enrollments = Enrollment.objects.count()

    context = {

        "total_users": total_users,
        "total_courses": total_courses,
        "total_enrollments": total_enrollments

    }

    return render(request, "dashboard.html", context)
