"""
Module where models are imported for django
"""

# user's profile
from .profile.profile import Profile

# car showroom models
from .car_showroom.car_showroom import CarShowroom
from .car_showroom.car_showroom_vehicle import CarShowroomVehisle
from .car_showroom.car_showroom_special_offer import CarShowroomSpecialOffer

# provider models
from .provider.provider import Provider
from .provider.provider_vehicle import ProviderVehicle
from .provider.provider_special_offer import ProviderSpecialOffer
from .provider.provider_discount import ProviderDiscount

# m2m model between car showroom and provider
from .m2m.car_showroom_provider import CarShowroomProvider

# purchase history models
from .purchase_history.user_purchase_history import UserPurchaseHistory
from .purchase_history.provider_purchase_history import ProviderPurchaseHistory

# vehicle characteristics
from .car_showroom.desired_vehicle_characteristics import (
    DesiredVehicleCharacteristics,
)
from .car_showroom.car_showroom_vehicle_characteristics import (
    CarShowroomVehicleCharacteristics,
)
from .provider.provider_vehicle_characteristics import (
    ProviderVehicleCharacteristics,
)

# model just to check how static files are managed
from .attachment_sample import AttachmentSample
