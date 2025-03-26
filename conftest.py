import pytest
import helper
import urls
import requests


@pytest.fixture
def delete_courier():
    payload = {'login': helper.generate_random_string(10),
               'password': helper.generate_random_string(10),
               'first_name': helper.generate_random_string(10)
               }
    yield payload
    response = requests.post(urls.MAIN_URL + '/api/v1/courier/login',
                             data={'login': payload['login'],
                                   'password': payload['password']})
    id = response.json()['id']
    requests.delete(urls.MAIN_URL + f'/api/v1/courier/{id}')


@pytest.fixture
def signed_up_courier():
    login = helper.generate_random_string(10)
    password = helper.generate_random_string(10)
    first_name = helper.generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier',
                             data=payload)
    login_pass = []
    if response.status_code == 201:
        login_pass.append(login)
        login_pass.append(password)
        login_pass.append(first_name)
    yield login_pass
    response = requests.post(urls.MAIN_URL + '/api/v1/courier/login',
                             data={'login': payload['login'],
                                   'password': payload['password']})
    id = response.json()['id']
    requests.delete(urls.MAIN_URL + f'/api/v1/courier/{id}')

