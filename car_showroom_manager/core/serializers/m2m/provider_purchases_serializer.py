"""
Module with provider purchase serializer
"""

from rest_framework.serializers import ModelSerializer

from core.models import CarShowroomProvider
from core.serializers.provider import ProviderSerializer


class ProviderPurchasesSeriaizer(ModelSerializer):
    """
    Provider purchase serializer
    """

    provider = ProviderSerializer(many=False)

    class Meta:
        model = CarShowroomProvider
        fields = [
            "provider",
            "number_of_purchases",
        ]
