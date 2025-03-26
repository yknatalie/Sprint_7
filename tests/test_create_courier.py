import urls
import requests
import helper
import allure


class TestCreateCourier:

    @allure.title("Успешное создание курьера")
    def test_create_courier_success(self, delete_courier):
        r = requests.post(urls.MAIN_URL + urls.CREATE_COURIER_ENDPOINT, data=delete_courier)
        assert r.status_code == 201 and r.json() == {'ok': True}

    @allure.title("Ошибка при попытке создания двух одинаковых курьеров")
    def test_creating_two_equal_couriers_error(self, delete_courier):
        requests.post(urls.MAIN_URL + urls.CREATE_COURIER_ENDPOINT, data=delete_courier)
        second_response = requests.post(urls.MAIN_URL + urls.CREATE_COURIER_ENDPOINT,
                                        data=delete_courier)

        assert (second_response.status_code == 409 and second_response.json() ==
                {'code': 409, 'message': 'Этот логин уже используется. Попробуйте другой.'})

    @allure.title("Ошибка при отсутствии логина в теле запроса при создании курьера")
    def test_no_login_error(self):
        password = helper.generate_random_string(10)
        first_name = helper.generate_random_string(10)
        r = requests.post(urls.MAIN_URL + urls.CREATE_COURIER_ENDPOINT, data={'password': password,
                                                                              'first_name': first_name})
        assert r.status_code == 400 and r.json() == {"code": 400,
                                                     "message": "Недостаточно данных для создания учетной записи"}

    @allure.title("Ошибка при отсутствии пароля в теле запроса при создании курьера")
    def test_no_password_error(self):
        login = helper.generate_random_string(10)
        first_name = helper.generate_random_string(10)
        r = requests.post(urls.MAIN_URL + urls.CREATE_COURIER_ENDPOINT, data={'login': login,
                                                                              'first_name': first_name})
        assert r.status_code == 400 and r.json() == {"code": 400,
                                                     "message": "Недостаточно данных для создания учетной записи"}

    @allure.title("Ошибка при отсутствии имени в теле запроса при создании курьера")
    def test_no_first_name_error(self):
        login = helper.generate_random_string(10)
        password = helper.generate_random_string(10)
        r = requests.post(urls.MAIN_URL + urls.CREATE_COURIER_ENDPOINT, data={'login': login,
                                                                              'password': password})
        assert r.status_code == 400 and r.json() == {"code": 400,
                                                     "message": "Недостаточно данных для создания учетной записи"}

    @allure.title("Ошибка при создании курьера с существующим логином")
    def test_same_login_two_couriers_error(self, delete_courier):
        password = helper.generate_random_string(10)
        first_name = helper.generate_random_string(10)
        r = requests.post(urls.MAIN_URL + urls.CREATE_COURIER_ENDPOINT, data=delete_courier)
        res = requests.post(urls.MAIN_URL + urls.CREATE_COURIER_ENDPOINT,
                            data={'login': delete_courier['login'],
                                  'password': password,
                                  'first_name': first_name})
        assert res.status_code == 409 and res.json() == {'code': 409,
                                                         'message': 'Этот логин уже используется. Попробуйте другой.'}
