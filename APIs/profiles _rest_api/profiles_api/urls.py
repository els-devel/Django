from django.urls import path, include
from profiles_api import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('secrets-viewset', views.SecretsViewSet, base_name='secrets-viewset')
router.register('profile', views.UserProfileViewSet) # we dont need a base name because
# we have a queryset, so django_rest_framework can figure out the name from the model that is assigned to it

urlpatterns = [
    path('heartbeat/', views.Heartbeat.as_view()),
    path('secrets-api', views.SecretsEngine.as_view()),
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls))
]
