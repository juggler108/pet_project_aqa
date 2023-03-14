import datetime
from random import randint, choice
from faker import Faker
from data.data import Person, ColorName, Date
from datetime import datetime

faker = Faker('ru_RU')
faker_en = Faker('EN')
# Faker.seed(0)


def generated_person():
    yield Person(
        full_name=faker.name(),
        first_name=faker.first_name(),
        last_name=faker.last_name(),
        email=faker.email(),
        phone_number=faker.msisdn(),
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


def generated_color():
    yield ColorName(
        color_name=["red", "Red", "Blue", "Green", "Yellow", "Purple",
                    "Black", "White", "Voilet", "Indigo", "Magenta", "Aqua"]
    )


def generated_date():
    yield Date(
        year=faker_en.year(),
        month=faker_en.month_name(),
        day=faker_en.day_of_month(),
        time="12:00"
    )


def time_list_15_min_interval():
    start_time = datetime.time(hour=0, minute=0, second=0)
    end_time = datetime.time(hour=23, minute=45, second=0)
    delta = datetime.timedelta(minutes=15)

    time_list = []
    current_time = start_time
    while current_time < end_time:
        time_list.append(current_time.strftime("%H:%M"))
        current_time = (datetime.datetime.combine(datetime.date.today(), current_time) + delta).time()
    return choice(time_list)
