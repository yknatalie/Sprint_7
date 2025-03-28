import allure

import urls
import requests
import pytest
from data import Data


class TestOrder:

    @allure.title("Успешное создание заказа")
    @pytest.mark.parametrize(
        'first_name, last_name, address, metro_station, phone,rent_time, delivery_date,comment,color',
        [Data.data_1, Data.data_2, Data.data_3])
    def test_create_order_success(self, first_name, last_name, address, metro_station, phone,
                                  rent_time, delivery_date, comment, color):
        r = requests.post(urls.MAIN_URL + urls.CREATE_ORDER, json={'firstName': first_name,
                                                                   'lastName': last_name,
                                                                   'address': address,
                                                                   'metroStation': metro_station,
                                                                   'phone': phone,
                                                                   'rentTime': rent_time,
                                                                   "deliveryDate": delivery_date,
                                                                   "comment": comment,
                                                                   "color": color})

        assert r.status_code == 201 and 'track' in r.json()
