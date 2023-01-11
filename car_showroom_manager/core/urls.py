"""
Core application urls
"""

from rest_framework_nested import routers

from core.views import CarShowroomViewSet
from core.views import ProviderViewSet
from core.views import ConsumerViewSet
from core.views import VehicleViewSet
from core.views import DesiredVehicleCharacteristicsViewSet


car_showroom_router = routers.SimpleRouter()
car_showroom_router.register(r"car-showrooms", CarShowroomViewSet)

provider_router = routers.SimpleRouter()
provider_router.register(r"providers", ProviderViewSet)

consumer_router = routers.SimpleRouter()
consumer_router.register(r"consumers", ConsumerViewSet)

car_showroom_vehicle_router = routers.NestedSimpleRouter(
    car_showroom_router, r"car-showrooms", lookup="user"
)
car_showroom_vehicle_router.register(
    r"vehicles", VehicleViewSet, basename="car-showroom-vehicle"
)

provider_vehicle_router = routers.NestedSimpleRouter(
    provider_router, r"providers", lookup="user"
)
provider_vehicle_router.register(
    r"vehicles", VehicleViewSet, basename="provider-vehicle"
)

car_showroom_desired_characteristics_router = routers.NestedSimpleRouter(
    car_showroom_router, r"car-showrooms", lookup="car_showroom"
)
car_showroom_desired_characteristics_router.register(
    r"desired-characteristics",
    DesiredVehicleCharacteristicsViewSet,
    basename="car-showroom-desired-characteristics",
)

urlpatterns = []
urlpatterns += car_showroom_router.urls
urlpatterns += provider_router.urls
urlpatterns += consumer_router.urls
urlpatterns += car_showroom_vehicle_router.urls
urlpatterns += provider_vehicle_router.urls
urlpatterns += car_showroom_desired_characteristics_router.urls
