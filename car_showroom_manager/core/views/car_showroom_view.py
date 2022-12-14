"""
Module with car showroom view
"""

from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser

from core.models import CarShowroom
from core.models import CarShowroomProfile
from core.serializers import CarShowroomSerializer
from core.serializers import ProviderPurchasesSeriaizer
from core.serializers import CarShowroomProfileSerializer
from core.services import get_purchases_response
from core.services import get_profile_response


class CarShowroomViewSet(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    """
    Car showroom list generic view set
    """

    queryset = CarShowroom.objects.all()
    serializer_class = CarShowroomSerializer
    permission_classes = [IsAdminUser]

    @action(detail=True, url_path="providers")
    def get_providers(self, request, pk=None):
        """Return providers with number of purchases"""

        return get_purchases_response(
            ProviderPurchasesSeriaizer, car_showroom__pk=pk
        )

    @action(detail=True, url_path="profile")
    def get_profile(self, request, pk=None):
        """Return car showroom's profile"""

        return get_profile_response(
            CarShowroomProfileSerializer,
            CarShowroomProfile,
            car_showroom__pk=pk,
        )
