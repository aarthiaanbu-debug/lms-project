from django.db import models
from django.contrib.auth.models import User


# -----------------------
# Course Model
# -----------------------
class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='course_images/')
    is_premium = models.BooleanField(default=False)

    def __str__(self):
        return self.title


# -----------------------
# Lesson Model
# -----------------------
class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    video = models.FileField(upload_to='lesson_videos/')

    def __str__(self):
        return self.title


# -----------------------
# Enrollment Model
# -----------------------
class Enrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrolled_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'course')

    def __str__(self):
        return f"{self.user.username} enrolled in {self.course.title}"


# -----------------------
# Progress Model
# -----------------------
class Progress(models.Model):
    enrollment = models.OneToOneField(Enrollment, on_delete=models.CASCADE)
    completed_lessons = models.IntegerField(default=0)
    progress_percent = models.FloatField(default=0)

    def __str__(self):
        return f"{self.enrollment.user.username} - {self.progress_percent}%"


# -----------------------
# Subscription Plan
# -----------------------
class Plan(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    duration_days = models.IntegerField()

    def __str__(self):
        return self.name


# -----------------------
# User Subscription
# -----------------------
class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.username} - {self.plan.name}"


# -----------------------
# Payment Model
# -----------------------
class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.amount}"
    class Progress(models.Model):

     user = models.ForeignKey(User,on_delete=models.CASCADE)

    course = models.ForeignKey(Course,on_delete=models.CASCADE)

    completed_lessons = models.IntegerField(default=0)

    percent = models.IntegerField(default=0)