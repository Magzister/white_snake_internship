"""
Module with car showroom proxy model
"""

from django.contrib.auth.models import UserManager

from core.models.user import User


class CarShowroomManager(UserManager):
    """
    Manager with redefined get_queryset mathod
    """

    def get_queryset(self, *args, **kwargs):
        """
        Method overrided to return users with user_type = CAR_SHOWROOM
        """

        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(user_type=User.Types.CAR_SHOWROOM)
        return queryset


class CarShowroom(User):
    """
    Proxy model to represent car showroom as a user
    """

    objects: UserManager = CarShowroomManager()

    def save(self, *args, **kwargs):
        """
        Method to set user_type as a car_showroom during saving a user
        """

        if not self.id:
            self.user_type = User.Types.CAR_SHOWROOM
        return super().save(*args, **kwargs)

    class Meta:
        proxy = True
