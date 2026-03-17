from django.urls import path
from . import views

urlpatterns = [

    path("dashboard/", views.dashboard, name="dashboard")

]
from django.urls import path
from .views import analytics_view

urlpatterns = [
    path('', analytics_view),
]