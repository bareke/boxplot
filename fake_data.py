from random import randint
from decimal import Decimal


class FakeData:
    def generate_data(self, min_value: int, max_value: int, limit_value: int) -> list:
        numbers = []

        for index in range(limit_value):
            random = randint(min_value, max_value)
            numbers.append(random)

        return numbers

    def load_data_pre(self, path: str) -> list:
        content = None

        with open(path) as file:
            content = file.readlines()

        # numbers = content.strip()
        # numbers = [mp.mpf(numero) for numero in numbers]
        numbers = [Decimal(linea.strip()) for linea in content]

        return numbers


    def load_data(self, path: str) -> list:
        content = None

        with open(path) as file:
            content = file.read()

        numbers = content.strip().split('\n')
        numbers = [(numero) for numero in numbers]

        return numbers
