from random import randint
from faker import Faker
from data.data import Person

faker = Faker('ru_RU')
# Faker.seed(0)


def generated_person():
    yield Person(
        full_name=faker.name(),
        first_name=faker.first_name(),
        last_name=faker.last_name(),
        email=faker.email(),
        age=randint(10, 80),
        salary=randint(1000, 5000),
        department=faker.job(),
        current_address=faker.address(),
        permanent_address=faker.address()
    )


def generated_file():
    path = rf"C:\python_projects\pet_project_aqa\filetest{randint(0, 777)}.txt"
    with open(path, "w+") as my_file:
        my_file.write(f"Hello world{randint(0, 777)}")

    return my_file.name, path
