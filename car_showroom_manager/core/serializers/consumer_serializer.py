"""
Module with consumer serializer
"""

from rest_framework.serializers import ModelSerializer

from core.models import Consumer


class ConsumerSerializer(ModelSerializer):
    """
    Consumer serializer
    """

    class Meta:
        model = Consumer
        fields = [
            "id",
            "username",
            "email",
        ]
