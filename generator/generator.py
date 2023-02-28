from faker import Faker

from data.data import Person

faker = Faker('ru_RU')
# Faker.seed(0)


def generated_person():
    yield Person(
        full_name=f"{faker.name()}",
        email=faker.email(),
        current_address=faker.address(),
        permanent_address=faker.address()
    )
