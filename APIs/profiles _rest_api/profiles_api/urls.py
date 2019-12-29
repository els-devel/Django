from django.urls import path
from profiles_api import views

urlpatterns = [
    path('heartbeat/', views.Heartbeat.as_view()),
    path('eric/', views.Eric.as_view())
]
