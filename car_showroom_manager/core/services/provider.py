"""
Services for provider
"""

from typing import Type
from rest_framework.response import Response

from core.models import ProviderDiscount
from core.serializers import ProviderDiscountSerializer

Discount = Type[ProviderDiscount]
Serializer = Type[ProviderDiscountSerializer]


def get_discounts_response(
    serializer: Serializer, discount: Discount, **kwargs
) -> Response:
    """
    Return response with provider's discounts
    """
    discounts = discount.objects.filter(**kwargs)
    discount_serializer = serializer(discounts, many=True)
    return Response(discount_serializer.data)
