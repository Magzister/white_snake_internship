"""
Module with provider serializer
"""

from rest_framework.serializers import ModelSerializer

from core.models import Provider


class ProviderSerializer(ModelSerializer):
    """
    Provider serializer
    """

    class Meta:
        model = Provider
        fields = [
            "id",
            "username",
            "email",
        ]
