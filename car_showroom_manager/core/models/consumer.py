"""
Module with consumer model
"""

from django.contrib.auth.models import UserManager

from core.models.user import User


class ConsumerManager(UserManager):
    """
    Manager with redefined get_queryset method
    """

    def get_queryset(self, *args, **kwargs):
        """
        Method overrided to return users with user_type = CONSUMER
        """

        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(user_type=User.Types.CONSUMER)
        return queryset


class Consumer(User):
    """
    Model to represent consumer
    """

    objects: UserManager = ConsumerManager()

    def save(self, *args, **kwargs):
        """
        Method to set user_type as a consumer during saving a user
        """

        if not self.id:
            self.user_type = User.Types.CONSUMER
        return super().save(*args, **kwargs)

    class Meta:
        proxy = True
