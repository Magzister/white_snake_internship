"""
Module with Desired vehicle characteristics view
"""

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser

from core.models import DesiredVehicleCharacteristics
from core.serializers import DesiredVehicleCharacteristicsSerializer


class DesiredVehicleCharacteristicsViewSet(ModelViewSet):
    """
    Desired vehicle characteristics view set
    """

    serializer_class = DesiredVehicleCharacteristicsSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        """Return desired characteristics"""

        return DesiredVehicleCharacteristics.objects.filter(
            car_showroom__pk=self.kwargs["car_showroom_pk"]
        )
