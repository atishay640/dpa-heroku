from rest_framework import routers
from sales.api.viewsets import UserViewSet

router = routers.SimpleRouter()
router.register('users', UserViewSet, basename='user')
urlpatterns = router.urls