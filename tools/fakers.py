from faker import Faker

fake = Faker("ru_RU")


def generate_email():
    return fake.email()

def generate_password():
    return '111111' #при необходимости fake.password()

def generate_first_name():
    return fake.first_name()

def generate_first_name_female():
    return fake.first_name_female()

def generate_last_name():
    return fake.last_name_male()

def generate_last_name_female():
    return fake.last_name_female()

def generate_middle_name():
    return fake.middle_name_male()