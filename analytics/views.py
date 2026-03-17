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
import requests
from django.shortcuts import render

def analytics_view(request):
    response = requests.get("http://127.0.0.1:8001/analytics")
    data = response.json()
    return render(request, "analytics.html", {"data": data})