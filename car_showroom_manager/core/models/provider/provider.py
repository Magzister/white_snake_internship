"""
Module with provider model
"""

from django.contrib.auth.models import UserManager

from core.models.user import User


class ProviderManager(UserManager):
    """
    Manager with redefined get_queryset method
    """

    def get_queryset(self, *args, **kwargs):
        """
        Method overrided to return users with user_type = PROVIDER
        """

        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(user_type=User.Types.PROVIDER)
        return queryset


class Provider(User):
    """
    Proxy model to represent provider as a user
    """

    objects: UserManager = ProviderManager()

    def save(self, *args, **kwargs):
        """
        Method to set user_type as a provider during saving a user
        """

        if not self.id:
            self.user_type = User.Types.PROVIDER
        return super().save(*args, **kwargs)

    class Meta:
        proxy = True
