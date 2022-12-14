"""
Module with consumer view
"""

from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser

from core.models import Consumer
from core.models import ConsumerProfile
from core.serializers import ConsumerSerializer
from core.serializers import ConsumerProfileSerializer
from core.services import get_profile_response


class ConsumerViewSet(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    """
    Consumer list generic view set
    """

    queryset = Consumer.objects.all()
    serializer_class = ConsumerSerializer
    permission_classes = [IsAdminUser]

    @action(detail=True, url_path="profile")
    def get_profile(self, request, pk=None):
        """Return consumer's profile"""

        return get_profile_response(
            ConsumerProfileSerializer, ConsumerProfile, consumer__pk=pk
        )
