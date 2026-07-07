from faker import Faker

class Fake:
    """
    Класс для генерации случайных тестовых данных с использованием
    """
    def __init__(self, faker:Faker):
        self.faker = faker

    def email(self) -> str:
        """
        Метод для генерации случайных почтовых адресов
        """
        return self.faker.email()

    def password(self)-> str:
        """
        Метод для генерации случайных паролей
        """
        return self.faker.password()

    def first_name(self)-> str:
        """
        Метод для генерации случайных мужских имен
        """
        return self.faker.first_name()

    def first_name_female(self)-> str:
        """
        Метод для генерации случайных женских имен
        """
        return self.faker.first_name_female()

    def last_name(self)-> str:
        """
        Метод для генерации случайных мужских фамилий
        """
        return self.faker.last_name_male()

    def last_name_female(self)-> str:
        """
        Метод для генерации случайных женских фамилий
        """
        return self.faker.last_name_female()

    def middle_name(self)-> str:
        """
        Метод для генерации случайных мужских отчеств
        """
        return self.faker.middle_name_male()

    def middle_name_female(self)-> str:
        """
        Метод для генерации случайных женских отчеств
        """
        return self.faker.middle_name_female()

    def text(self)-> str:
        """
        Метод для генерации случайных текстов
        """
        return self.faker.text()

    def sentence(self)-> str:
        """
        Метод для генерации случайных предложений
        """
        return self.faker.sentence()

    def estimated_time(self)-> str:
        """
        Метод для генерации случайных данных для поля Оценка времени
        """
        return f"{self.integer(1, 1000)} Hours"

    def integer(self, min_value = 1, max_value = 100)-> int:
        """
        Метод для генерации случайных чисел
        """
        return self.faker.random_int(min_value, max_value)

    def max_score(self)-> int:
        """
        Метод для генерации случайных чисел для поля Максимальной оценки
        """
        return self.integer(50, 100)

    def min_score(self)-> int:
        """
        Метод для генерации случайных чисел для поля Минимальной оценки
        """
        return self.integer(1, 10)

    def uuid4(self)-> str:
        """
        Метод для генерации случайных значений для полей uuid4
        """
        return self.faker.uuid4()

    def word(self)->str:
        return self.faker.word()






fake = Fake(faker=Faker("ru_RU"))