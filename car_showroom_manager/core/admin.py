"""
Module with admin registered models
"""

from django.contrib import admin

from core.models import CarShowroomProvider

from core.models import CarShowroom
from core.models import SpecialOffer

from core.models import Vehicle
from core.models import UserVehicleCharacteristics
from core.models import DesiredVehicleCharacteristics

from core.models import Provider
from core.models import ProviderDiscount

from core.models import User

from core.models import ConsumerProfile
from core.models import CarShowroomProfile
from core.models import ProviderProfile

from core.models import Consumer

from core.models import PurchaseHistory


admin.site.register(CarShowroomProvider)

admin.site.register(CarShowroom)

admin.site.register(SpecialOffer)
admin.site.register(Vehicle)
admin.site.register(UserVehicleCharacteristics)
admin.site.register(DesiredVehicleCharacteristics)

admin.site.register(User)

admin.site.register(Provider)
admin.site.register(ProviderDiscount)

admin.site.register(ConsumerProfile)
admin.site.register(CarShowroomProfile)
admin.site.register(ProviderProfile)

admin.site.register(Consumer)
admin.site.register(PurchaseHistory)
