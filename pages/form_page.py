import os
from random import randint
from time import sleep

from selenium.webdriver import Keys

from generator.generator import generated_person, generated_file
from locators.form_page_locators import FormPageLocators
from pages.base_page import BasePage


class FormPage(BasePage):
    locators = FormPageLocators()

    def fill_all_form_fields(self):
        person = next(generated_person())
        file_name, path = generated_file()
        self.remove_footer()
        self.element_is_visible(self.locators.FIRST_NAME).send_keys(person.first_name)
        self.element_is_visible(self.locators.LAST_NAME).send_keys(person.last_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(person.email)
        self.element_is_visible(self.locators.GENDER_RADIO).click()
        self.element_is_visible(self.locators.MOBILE).send_keys(person.phone_number)
        self.element_is_visible(self.locators.SUBJECT_INPUT).send_keys(self.locators.SUBJECT_DICT[randint(1, 14)])
        self.element_is_visible(self.locators.SUBJECT_INPUT).send_keys(Keys.RETURN)
        self.element_is_visible(self.locators.HOBBIES_CHECKBOX).click()
        self.element_is_present(self.locators.UPLOAD_PICTURE).send_keys(path)
        os.remove(path=path)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(person.current_address)
        self.element_is_visible(self.locators.STATE_SELECT).click()
        self.element_is_visible(self.locators.STATE_INPUT).send_keys(Keys.RETURN)
        self.element_is_visible(self.locators.CITY_SELECT).click()
        self.element_is_visible(self.locators.CITY_INPUT).send_keys(Keys.RETURN)
        self.element_is_visible(self.locators.SUBMIT).click()
        return [person.first_name, person.last_name, person.email]

    def get_table_result(self):
        table_result = self.elements_are_visible(self.locators.TABLE_RESULT)
        data = []
        for result in table_result:
            data.append(result.text)
        return data



