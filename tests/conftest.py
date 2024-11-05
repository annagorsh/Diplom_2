import string
import pytest
import random
from random import randint


@pytest.fixture
def payload():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    email = str(randint(10000, 99999)) + "@gmail.com"
    password = str(randint(1000000, 9999999))
    name = generate_random_string(10)

    payload = {
        "email": email,
        "password": password,
        "name": name
    }

    return payload

@pytest.fixture
def rand_name():
    rand_name = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10))
    return rand_name

@pytest.fixture
def incomplete_user_data():
    email = str(randint(10000, 99999)) + "@gmail.com"
    password = str(randint(1000000, 9999999))
    incomplete_user_data = {
        "email": email,
        "password": password
    }
    return incomplete_user_data
