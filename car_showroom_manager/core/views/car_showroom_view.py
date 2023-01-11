"""
Module with car showroom view
"""

from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser

from core.models import CarShowroom
from core.models import CarShowroomProfile
from core.models import DesiredVehicleCharacteristics
from core.models import CarShowroomProvider
from core.serializers import CarShowroomSerializer
from core.serializers import ProviderPurchasesSeriaizer
from core.serializers import CarShowroomProfileSerializer
from core.serializers import DesiredVehicleCharacteristicsSerializer
from core.services import get_object_response
from .custom_viewset import RetrieveUpdateDestroyListVireSet


class CarShowroomViewSet(RetrieveUpdateDestroyListVireSet):
    """
    Car showroom list generic view set
    """

    queryset = CarShowroom.objects.all()
    serializer_class = CarShowroomSerializer
    permission_classes = [IsAdminUser]

    @action(detail=True, url_path="providers")
    def get_providers(self, request, pk=None):
        """Return providers with number of purchases"""

        return get_object_response(
            ProviderPurchasesSeriaizer,
            CarShowroomProvider,
            many=True,
            car_showroom__pk=pk,
        )

    @action(detail=True, url_path="profile")
    def get_profile(self, request, pk=None):
        """Return car showroom's profile"""

        return get_object_response(
            CarShowroomProfileSerializer,
            CarShowroomProfile,
            many=False,
            car_showroom__pk=pk,
        )

    @action(detail=True, url_path="desired-vehicle-characteristics")
    def get_desired_vehicle_characteristics(self, request, pk=None):
        """Return desired vehicle characteristics"""

        return get_object_response(
            DesiredVehicleCharacteristicsSerializer,
            DesiredVehicleCharacteristics,
            many=True,
            car_showroom__id=pk,
        )
