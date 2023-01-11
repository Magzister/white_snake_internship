"""
Module with vehicle view
"""

from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser

from core.models import Vehicle
from core.models import UserVehicleCharacteristics
from core.serializers import VehicleSerializer
from core.serializers import VehicleCharacteristicsSerializer
from core.services import get_object_response


class VehicleViewSet(ModelViewSet):
    """
    Vehicle view set
    """

    serializer_class = VehicleSerializer
    permission_classes = [IsAdminUser]

    def perform_create(self, serializer):
        """Saving a new object instance"""

        serializer.save(user=self.request.user)

    def get_queryset(self):
        """Return vehicle queryset"""

        return Vehicle.objects.filter(user__pk=self.kwargs["user_pk"])

    @action(detail=True, url_path="characteristics")
    def get_characteristics(self, request, user_pk=None, pk=None):
        """Return vehicle characteristics"""
        return get_object_response(
            VehicleCharacteristicsSerializer,
            UserVehicleCharacteristics,
            many=False,
            vehicle__pk=pk,
        )
