from rest_framework.routers import DefaultRouter

from apps.main.views import MainApiViewSet, ConsultationApiViewSet


router = DefaultRouter()
router.register(
    prefix="order",
    viewset=MainApiViewSet
)

router.register(
    prefix="consultation",
    viewset=ConsultationApiViewSet
)

urlpatterns = router.urls
