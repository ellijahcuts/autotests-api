import pytest


@pytest.fixture(autouse=True)
def send_analitics_data():
    print('[AUTOUSE] Отправка аналитики')

@pytest.fixture(autouse=True,scope='session')
def settings():
    print('[SESSION] Инициализация настроек для сессии')

@pytest.fixture(autouse=True,scope="class")
def user():
    print("[CLASS] Создаем данные пользака для каждого класса, 1 раз")

@pytest.fixture(autouse=True,scope="function")
def user_client(settings):
    print("[FUNCTION] Создаем АПИ клиент на каждый тест")

class TestUserFlow:
    def test_user_can_login(self, settings, user, user_client):
        ...

    def test_user_can_create_course(self,settings,user, user_client):
        ...

class TestAccountFlow:
    def test_user_account(self, settings,user, user_client):
        ...

@pytest.fixture
def user_data()->dict:
    print('Создаем пользователя до теста (setup)')
    yield {'username': 'test', 'password': '1234', 'email': 'asdasfg'}
    print("Удаляем данные после теста(teardown)")

def test_user_email(user_data: dict):
    assert user_data['email'] == 'asdasfg'

def test_user_password(user_data: dict):
    assert user_data['password'] == '1234'

def test_user_name(user_data: dict):
    assert user_data['username'] == 'test'