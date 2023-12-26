from .apps import AppConfig
from rest_framework.routers import DefaultRouter
from .views import LinkViewSet, ContactViewSet, ProductViewSet

app_name = AppConfig.name

router = DefaultRouter()
router.register(r'links', LinkViewSet, basename='links')
router.register(r'contacts', ContactViewSet, basename='contacts')
router.register(r'product', ProductViewSet, basename='product')

urlpatterns = [
              ] + router.urls
