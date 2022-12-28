"""
Module where models are imported for django
"""

from core.models.user import User

from core.models.profile import ConsumerProfile
from core.models.profile import CarShowroomProfile
from core.models.profile import ProviderProvile

from core.models.consumer import Consumer

from core.models.car_showroom import CarShowroom

from core.models.special_offer import SpecialOffer

from core.models.provider import Provider
from core.models.provider import ProviderDiscount

from core.models.m2m import CarShowroomProvider

from core.models.purchase_history import PurchaseHistory

from core.models.vehicle import Vehicle
from core.models.vehicle import UserVehicleCharacteristics
from core.models.vehicle import DesiredVehicleCharacteristics

from core.models.attachment_sample import AttachmentSample
