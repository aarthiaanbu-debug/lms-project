"""
URL configuration for learning project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
"""
URL configuration for learning project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from lms_admin import views
from django.urls import path, include


urlpatterns = [

    path('admin/', admin.site.urls),

    path('', views.home, name='home'),

    path('courses/', views.course_list, name='courses'),

    path('course/<int:id>/', views.course_detail, name='course_detail'),

    path('enroll/<int:course_id>/', views.enroll, name='enroll'),

    path('lesson/<int:id>/', views.lesson_video, name='lesson_video'),

    path('complete/<int:lesson_id>/', views.complete_lesson, name='complete_lesson'),

    path('dashboard/', views.dashboard, name='dashboard'),
    path('analytics/', include('analytics.urls')),

]
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lms/', include('lms_admin.urls')),
]
from django.urls import path, include

urlpatterns = [
    path('lms/', include('lms_admin.urls')),
]

# Media Files
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)