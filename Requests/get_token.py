import requests

url = 'http://5.101.50.27:8000'
creds = {
    "username": "harrypotter",
    "password": "expelliarmus"
}


# получение токена
def get_token(url, creds):
    resp = requests.post(f'{url}/auth/login', json=creds)
    print(resp.json()['user_token'])
    return resp.json()['user_token']


token = get_token(url, creds)


# получение списка компаний
def get_company_list():
    resp = requests.get(f'{url}/company/list')
    print(resp.json())
    return resp.json()


list = get_company_list()


id = 801


# получение компании по id
def get_comp_by_id(id):
    try:
        # выполняем запрос
        resp = requests.get(f'{url}/company/{id}')
        # проверяем статус ответа
        if resp.status_code == 404:
            # если данное условие выполняется поднимаем ошибку неверного
            # значения аргумента (ValueError)
            raise ValueError(f'Компания с id {id} не существует')
        elif resp.status_code != 200:
            # если статус код ответа не равен 200, поднимаем общую ошибку
            # (исключение) с выводом текста ответа
            raise Exception(f'Ошибка: {resp.status_code}. Ответ: {resp.text}')
        print(resp.json())
        # если всё в порядке, возвращаем данные компании
        return resp.json()
    except ValueError as e:
        # обрабатываем отсутствие компании
        print(e)
    except Exception as e:
        # обрабатываем другие ошибки
        print(f"Произошла ошибка: {e}")


company_by_id = get_comp_by_id(id)

# создание компании
body = {
    "name": "testAPI",
    "description": "string",
    "is_active": "true"
}


def create_company():
    resp = requests.post(f'{url}/company/create', json=body)
    print(resp.json())
    return resp.json()


cr_comp = create_company()


# данные о сотруднике по его ID
def get_employee_info(employee_id):
    resp = requests.get(f'{url}/employee/info/{employee_id}')
    return resp.json()


info = get_employee_info(1)
print(info)


# создание сотрудника с заданными параметрами
body = {
  "first_name": "A",
  "last_name": "B",
  "middle_name": "C",
  "company_id": 1,
  "email": "abc@example.com",
  "phone": "+79998881234",
  "birthdate": "2024-12-22",
  "is_active": "true"
}


def create_employee(body):
    resp = requests.post(f'{url}/employee/create', json=body)
    return resp.json()


create_employee = create_employee(body)
print(create_employee)


# список сотрудников по ID компании
def get_employee_list(company_id):
    resp = requests.get(f'{url}/employee/list/{company_id}')
    print(resp.status_code)
    print(resp.json())
    return resp.json()


emp = get_employee_list('jlby')


# изменение данных сотрудника
request_body = {
  "last_name": "ABC",
  "email": "abc@test.com",
  "phone": "string",
  "is_active": "true"
}


def change_employee(employee_id):
    resp = requests.patch(f'{url}/employee/change/{employee_id}\
                          ?client_token={token}', json=request_body)
    return resp.json()


ch_employee = change_employee(1)
print(ch_employee)
