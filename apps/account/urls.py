# Django
from rest_framework.routers import DefaultRouter

# Local
from apps.account.views import AccountViewSet

router = DefaultRouter()
router.register(r"picture", AccountViewSet)
urlpatterns = router.urls
