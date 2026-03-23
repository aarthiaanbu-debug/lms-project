from django.contrib import admin
from django.urls import path
from lms_admin import views

urlpatterns = [

    path('admin/', admin.site.urls),

    path('', views.home, name='home'),

    path('courses/', views.course_list, name='courses'),

    path('course/<int:id>/', views.course_detail, name='course_detail'),

    path('enroll/<int:course_id>/', views.enroll, name='enroll'),

    path('lesson/<int:id>/', views.lesson_video, name='lesson_video'),

    path('dashboard/', views.dashboard, name='dashboard'),

]
from django.urls import path
from .views import create_checkout_session, stripe_webhook, payment_page,success_page,cancel_page

urlpatterns = [
    path('create-checkout-session/', create_checkout_session),
    path('webhook/', stripe_webhook),
    path('payment-page/', payment_page),
    path('success/', success_page),
    path('cancel/', cancel_page),
]