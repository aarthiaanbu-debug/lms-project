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
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import stripe
from .models import Payment

stripe.api_key = "sk_test_51TCvrwIBSgL9ojRJ9AJBFCtRKuNTIdlhO99pHSS2GV9EmSOm2FrmSQxu4GFyUw1dSZQM7Uu04qSAgXzbgVliMmS500yLyoQgb0"
WEBHOOK_SECRET = "whsec_120ae124af1fb510750d45a3cb17ec38abc34f5b944ee28af688ac14dacff688"

@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.headers.get('stripe-signature')

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, WEBHOOK_SECRET
        )
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)

    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']

        Payment.objects.create(
            stripe_session_id=session['id'],
            amount=session['amount_total'] / 100,
            currency=session['currency'],
            status='success'
        )

    return JsonResponse({'status': 'success'})
import stripe
from django.conf import settings
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

stripe.api_key = settings.STRIPE_SECRET_KEY


# ✅ Create checkout session
def create_checkout_session(request):
    try:
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'inr',
                    'product_data': {
                        'name': 'Course Payment',
                    },
                    'unit_amount': 50000,
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url='http://127.0.0.1:8000/lms/success/',
            cancel_url='http://127.0.0.1:8000/lms/cancel/',
        )

        return JsonResponse({'id': session.id})

    except Exception as e:
        print("ERROR:", str(e))  # 👈 terminal la show aagum
        return JsonResponse({'error': str(e)}, status=500)


# ✅ Webhook
@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META.get('HTTP_STRIPE_SIGNATURE')
    endpoint_secret = settings.STRIPE_WEBHOOK_SECRET

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except Exception:
        return HttpResponse(status=400)

    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']

        from .models import Payment

        Payment.objects.create(
            stripe_session_id=session['id'],
            amount=session['amount_total'] / 100,
            currency=session['currency'],
            status='success'
        )

    return HttpResponse(status=200)
from django.shortcuts import render

def payment_page(request):
    return render(request, 'payment.html')
from django.shortcuts import render

def success_page(request):
    return render(request, 'success.html')

def cancel_page(request):
    return render(request, 'cancel.html')
