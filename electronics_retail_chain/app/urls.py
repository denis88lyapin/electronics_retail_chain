from django.urls import path
from .apps import AppConfig
from rest_framework.routers import DefaultRouter
from .views import LinkViewSet

app_name = AppConfig.name

router = DefaultRouter()
router.register(r'links', LinkViewSet, basename='links')

urlpatterns = [
] + router.urls