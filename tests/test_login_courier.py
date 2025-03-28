import urls
import requests
import helper
import allure

from data import Messages


class TestLoginCourier:

    @allure.title("Успешная авторизация курьера")
    def test_login_success(self, signed_up_courier):
        r = requests.post(urls.MAIN_URL + urls.SIGNED_IN_COURIER,
                          data={'login': signed_up_courier[0],
                                'password': signed_up_courier[1]})
        assert r.status_code == 200 and 'id' in r.text

    @allure.title("Ошибка при отсутствии пароля в теле запроса")
    def test_no_password_error(self, signed_up_courier):
        r = requests.post(urls.MAIN_URL + urls.SIGNED_IN_COURIER,
                          data={'login': signed_up_courier[0]})
        assert r.status_code == 400 and r.text == Messages.authorization_missing_parameter_error

    @allure.title("Ошибка при отсутствии логина в теле запроса")
    def test_no_login_error(self, signed_up_courier):
        r = requests.post(urls.MAIN_URL + urls.SIGNED_IN_COURIER,
                          data={'password': signed_up_courier[1]})
        assert r.status_code == 400 and r.text == Messages.authorization_missing_parameter_error

    @allure.title("Ошибка авторизации курьера с несуществующим логином")
    def test_not_existed_login_error(self):
        login = helper.generate_random_string(10)
        password = helper.generate_random_string(10)
        r = requests.post(urls.MAIN_URL + urls.SIGNED_IN_COURIER,
                          data={'login': login, 'password': password})
        assert r.status_code == 404 and r.text == Messages.authorization_no_profile_is_found
