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
    response = requests.post(urls.MAIN_URL + urls.SIGNED_IN_COURIER,
                             data={'login': payload['login'],
                                   'password': payload['password']})
    id = response.json()['id']
    requests.delete(urls.MAIN_URL + f'/api/v1/courier/{id}')


@pytest.fixture
def signed_up_courier(delete_courier):

    payload = delete_courier
    response = requests.post(urls.MAIN_URL + urls.CREATE_COURIER_ENDPOINT,
                             data=payload)
    login_pass = []
    if response.status_code == 201:
        login_pass.append(delete_courier['login'])
        login_pass.append(delete_courier['password'])
        login_pass.append(delete_courier['first_name'])
    yield login_pass


