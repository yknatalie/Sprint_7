import urls
import requests
import helper
import allure
from data import Messages, Data
import pytest


class TestCreateCourier:

    @allure.title("Успешное создание курьера")
    def test_create_courier_success(self, delete_courier):
        r = requests.post(urls.MAIN_URL + urls.CREATE_COURIER_ENDPOINT, data=delete_courier)
        assert r.status_code == 201 and r.json() == Messages.signed_up_courierr

    @allure.title("Ошибка при попытке создания двух одинаковых курьеров")
    def test_creating_two_equal_couriers_error(self, delete_courier):
        requests.post(urls.MAIN_URL + urls.CREATE_COURIER_ENDPOINT, data=delete_courier)
        second_response = requests.post(urls.MAIN_URL + urls.CREATE_COURIER_ENDPOINT,
                                        data=delete_courier)

        assert (second_response.status_code == 409 and second_response.json() == Messages.existed_login_error
                )

    @allure.title("Ошибка при отсутствии логина, пароля, имени в теле запроса при создании курьера")
    @pytest.mark.parametrize('login,password,first_name', [Data.lst_1, Data.lst_2, Data.lst_3])
    def test_no_login_error(self, login,password, first_name):
        r = requests.post(urls.MAIN_URL + urls.CREATE_COURIER_ENDPOINT, data={'login': login,
                                                                              'password': password,
                                                                              'first_name': first_name})
        assert r.status_code == 400 and r.json() == Messages.missing_parameter_error

    @allure.title("Ошибка при создании курьера с существующим логином")
    def test_same_login_two_couriers_error(self, delete_courier):
        password = helper.generate_random_string(10)
        first_name = helper.generate_random_string(10)
        r = requests.post(urls.MAIN_URL + urls.CREATE_COURIER_ENDPOINT, data=delete_courier)
        res = requests.post(urls.MAIN_URL + urls.CREATE_COURIER_ENDPOINT,
                            data={'login': delete_courier['login'],
                                  'password': password,
                                  'first_name': first_name})
        assert res.status_code == 409 and res.json() == Messages.existed_login_error
