from random import randint
from selenium.webdriver.common.by import By


class FormPageLocators:
    FIRST_NAME = (By.CSS_SELECTOR, "#firstName")
    LAST_NAME = (By.CSS_SELECTOR, "#lastName")
    EMAIL = (By.CSS_SELECTOR, "#userEmail")
    GENDER_RADIO = (By.CSS_SELECTOR, f"label[for='gender-radio-{randint(1,3)}']")
    MOBILE = (By.CSS_SELECTOR, "#userNumber")
    DATE_OF_BIRTH = (By.CSS_SELECTOR, "#dateOfBirthInput")
    SUBJECT_INPUT = (By.CSS_SELECTOR, "#subjectsInput")
    HOBBIES_CHECKBOX = (By.CSS_SELECTOR, f"label[for='hobbies-checkbox-{randint(1,3)}']")
    UPLOAD_PICTURE = (By.CSS_SELECTOR, "#uploadPicture")
    CURRENT_ADDRESS = (By.CSS_SELECTOR, "#currentAddress")
    STATE_SELECT = (By.CSS_SELECTOR, "#state")
    STATE_INPUT = (By.CSS_SELECTOR, "#react-select-3-input")
    CITY_SELECT = (By.CSS_SELECTOR, "#city")
    CITY_INPUT = (By.CSS_SELECTOR, "#react-select-4-input")
    SUBMIT = (By.CSS_SELECTOR, "#submit")

    SUBJECT_DICT = {1: 'Hindi', 2: 'English', 3: 'Maths', 4: 'Physics', 5: 'Chemistry',
                    6: 'Biology', 7: 'Computer Science', 8: 'Commerce', 9: 'Accounting',
                    10: 'Economics', 11: 'Arts', 12: 'Social Studies', 13: 'History', 14: 'Civics'}

    # result
    TABLE_RESULT = (By.XPATH, "//div/table/tbody/tr/td[2]")
