"""
Retrieve Update Destroy List ViewSet
"""

from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet


class RetrieveUpdateDestroyListVireSet(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    """
    Retrieve Update Destroy List ViewSet
    """

    pass
