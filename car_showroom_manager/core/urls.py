"""
Core application urls
"""

from rest_framework import routers

from core.views import CarShowroomViewSet
from core.views import ProviderViewSet
from core.views import ConsumerViewSet


router = routers.SimpleRouter()
router.register(r"car-showrooms", CarShowroomViewSet)
router.register(r"providers", ProviderViewSet)
router.register(r"consumers", ConsumerViewSet)

urlpatterns = router.urls
