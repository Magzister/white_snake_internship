"""
Module with provider view
"""

from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser

from core.models import Provider
from core.models import ProviderProfile
from core.models import ProviderDiscount
from core.models import CarShowroomProvider
from core.serializers import ProviderSerializer
from core.serializers import CarShowroomPurchasesSerializer
from core.serializers import ProviderProfileSerializer
from core.serializers import ProviderDiscountSerializer
from core.services import get_object_response
from .custom_viewset import RetrieveUpdateDestroyListVireSet


class ProviderViewSet(RetrieveUpdateDestroyListVireSet):
    """
    Provider list generic view set
    """

    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
    permission_classes = [IsAdminUser]

    @action(detail=True, url_path="car-showrooms")
    def get_car_showrooms(self, request, pk=None):
        """Return car showrooms with number of purchases"""

        return get_object_response(
            CarShowroomPurchasesSerializer,
            CarShowroomProvider,
            many=True,
            provider__pk=pk,
        )

    @action(detail=True, url_path="profile")
    def get_profile(self, request, pk=None):
        """Return provider's profile"""

        return get_object_response(
            ProviderProfileSerializer,
            ProviderProfile,
            many=False,
            provider__pk=pk,
        )

    @action(detail=True, url_path="discounts")
    def get_discounts(self, request, pk=None):
        """Return provider's discounts"""
        return get_object_response(
            ProviderDiscountSerializer,
            ProviderDiscount,
            many=True,
            provider__pk=pk,
        )
