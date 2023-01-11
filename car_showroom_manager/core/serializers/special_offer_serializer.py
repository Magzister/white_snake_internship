"""
Module with special offer serializer
"""

from rest_framework.serializers import ModelSerializer

from core.models import SpecialOffer


class SpecialOfferSerializer(ModelSerializer):
    """
    Special offer serializer
    """

    class Meta:
        model = SpecialOffer
        fields = [
            "id",
            "name",
            "vehicle",
            "description",
            "date_from",
            "date_to",
            "discount",
        ]
