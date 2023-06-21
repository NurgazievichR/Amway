from rest_framework.routers import DefaultRouter

from apps.categories.views import CategoryApiViewSet


router = DefaultRouter()
router.register(
    prefix="",
    viewset=CategoryApiViewSet
)

urlpatterns = router.urls
