import pytest

from core.models import CarShowroom
from core.models import CarShowroomProfile


@pytest.fixture
def admin_client(client, admin_user):
    client.force_login(admin_user)
    return client


@pytest.fixture
def car_showroom():
    car_showroom_profile_data = {
        "car_showroom_name": "test_car_showroom_name",
        "location_country": "BY",
        "location_city": "Minsk",
        "location_street": "Makayonka",
        "location_house": "9",
        "money": 100.00,
    }
    car_showroom_data = {
        "username": "test_car_showroom",
        "password": "test_password",
    }

    car_showroom = CarShowroom.objects.create(**car_showroom_data)
    car_showroom_profile = CarShowroomProfile.objects.create(
        **car_showroom_profile_data, car_showroom=car_showroom
    )

    return car_showroom
