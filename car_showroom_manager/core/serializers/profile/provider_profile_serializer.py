"""
Module with provider profile serializer
"""

from rest_framework.serializers import ModelSerializer

from core.models import ProviderProfile


class ProviderProfileSerializer(ModelSerializer):
    """
    Provider profile serializer
    """

    class Meta:
        model = ProviderProfile
        fields = [
            "id",
            "provider_name",
            "date_of_foundation",
            "number_of_buyers",
        ]
