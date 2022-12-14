"""
Module with provider view
"""

from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser

from core.models import Provider
from core.models import ProviderProfile
from core.serializers import ProviderSerializer
from core.serializers import CarShowroomPurchasesSerializer
from core.serializers import ProviderProfileSerializer
from core.services import get_purchases_response
from core.services import get_profile_response


class ProviderViewSet(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    """
    Provider list generic view set
    """

    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
    permission_classes = [IsAdminUser]

    @action(detail=True, url_path="car-showrooms")
    def get_car_showrooms(self, request, pk=None):
        """Return car showrooms with number of purchases"""

        return get_purchases_response(
            CarShowroomPurchasesSerializer, provider__pk=pk
        )

    @action(detail=True, url_path="profile")
    def get_profile(self, request, pk=None):
        """Return provider's profile"""

        return get_profile_response(
            ProviderProfileSerializer, ProviderProfile, provider__pk=pk
        )
