"""
Module with admin registered models
"""

from django.contrib import admin

from core.models import CarShowroomProvider

from core.models import CarShowroom
from core.models import CarShowroomSpecialOffer
from core.models import CarShowroomVehisle
from core.models import CarShowroomVehicleCharacteristics
from core.models import DesiredVehicleCharacteristics

from core.models import Provider
from core.models import ProviderSpecialOffer
from core.models import ProviderVehicle
from core.models import ProviderVehicleCharacteristics
from core.models import ProviderDiscount

from core.models import Profile

from core.models import UserPurchaseHistory
from core.models import ProviderPurchaseHistory


admin.site.register(CarShowroomProvider)

admin.site.register(CarShowroom)
admin.site.register(CarShowroomSpecialOffer)
admin.site.register(CarShowroomVehisle)
admin.site.register(CarShowroomVehicleCharacteristics)
admin.site.register(DesiredVehicleCharacteristics)

admin.site.register(Provider)
admin.site.register(ProviderSpecialOffer)
admin.site.register(ProviderVehicle)
admin.site.register(ProviderVehicleCharacteristics)
admin.site.register(ProviderDiscount)

admin.site.register(Profile)
admin.site.register(UserPurchaseHistory)
admin.site.register(ProviderPurchaseHistory)
