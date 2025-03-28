import helper

class Data:
    data_1 = ["Кирилл", "Иванов", "Ивановская 4", 5, "111111114581", 2, "12-05-2025", "вакккаэ",
              ["BLACK"]]
    data_2 = ["Ольга", "Кравцова", "Котова, 4", 6, '222222274822', 3, "09-09-2025", 'вакккаэ', []]
    data_3 = ["Ольг", "Кравца", "Кова, 4", 7, '222222964224', 4, '09-06-2025', 'вакккэ',
              ["BLACK", "GREY"]]

    lst_1 = [None, helper.generate_random_string(10), helper.generate_random_string(10)]
    lst_2 = [helper.generate_random_string(10), None, helper.generate_random_string(10)]
    lst_3 = [helper.generate_random_string(10), helper.generate_random_string(10), None]

class Messages:
    signed_up_courierr = {'ok': True}
    existed_login_error = {'code': 409, 'message': 'Этот логин уже используется. Попробуйте другой.'}
    missing_parameter_error = {"code": 400, "message": "Недостаточно данных для создания учетной записи"}
    authorization_missing_parameter_error = '{"code":400,"message": "Недостаточно данных для входа"}'
    authorization_no_profile_is_found = '{"code":404,"message":"Учетная запись не найдена"}'