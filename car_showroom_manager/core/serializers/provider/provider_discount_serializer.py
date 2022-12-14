"""
Module with provider discount serializer
"""

from rest_framework.serializers import ModelSerializer

from core.models import ProviderDiscount


class ProviderDiscountSerializer(ModelSerializer):
    """
    Provider discount serializer
    """

    class Meta:
        model = ProviderDiscount
        fields = [
            "id",
            "purchases_before_discount",
            "discount",
        ]
