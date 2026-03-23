from django.shortcuts import render
from .models import Notification
from django.contrib.auth.decorators import login_required

@login_required
def notification_list(request):

    notifications = Notification.objects.filter(user=request.user)

    return render(request, "notifications/list.html", {
        "notifications": notifications
    })