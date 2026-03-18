from django.contrib import admin
from .models import Course, Lesson, Enrollment, Progress, Plan, Subscription, Payment

admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Enrollment)
admin.site.register(Progress)
admin.site.register(Plan)
admin.site.register(Subscription)
admin.site.register(Payment)
from django.contrib import admin
from .models import SocialAccount, OTPLog

admin.site.register(SocialAccount)
admin.site.register(OTPLog)