"""
Services for user models with m2m relationship
"""

from typing import Union
from typing import Type
from rest_framework.response import Response

from core.models import CarShowroomProvider
from core.serializers import CarShowroomPurchasesSerializer
from core.serializers import ProviderPurchasesSeriaizer

Serializer = Union[
    Type[ProviderPurchasesSeriaizer], Type[CarShowroomPurchasesSerializer]
]


def get_purchases_response(serializer: Serializer, **kwargs) -> Response:
    """
    Return response with user models and their's purchases
    """
    users = CarShowroomProvider.objects.filter(**kwargs)
    user_serializer = serializer(users, many=True)
    return Response(user_serializer.data)
