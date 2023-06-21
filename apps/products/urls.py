from rest_framework.routers import DefaultRouter

from apps.products.views import ProductApiViewSet


router = DefaultRouter()
router.register(
    prefix="",
    viewset=ProductApiViewSet
)

urlpatterns = router.urls
