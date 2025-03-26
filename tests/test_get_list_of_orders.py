import urls
import requests
import allure



class TestGetOrdersList:

    @allure.title("Получаем список заказов и проверяем что в теле ответа есть объект orders")
    def test_get_list_of_orders(self):
        r = requests.get(urls.MAIN_URL + urls.CREATE_ORDER)
        assert "orders" in r.json()
