import pytest
from rest_framework.test import APIClient

from core.tests.fixtures import admin_client, car_showroom


class TestCarShowroom:
    @pytest.mark.django_db
    def test_car_showroom_list(self, admin_client, car_showroom):
        response = admin_client.get("/car-showrooms/")
        data = response.data
        receive_car_showroom = data[0]

        assert len(data) == 1
        assert receive_car_showroom["username"] == car_showroom.username
        assert (
            receive_car_showroom["profile"]["money"]
            == "%.2f" % car_showroom.car_showroom_profile.money
        )
        assert "password" not in receive_car_showroom
