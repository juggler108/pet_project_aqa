from time import sleep
from random import choice

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from generator.generator import generated_person
from locators.elements_page_locators import TextBoxPageLocators, CheckBoxPageLocators, RadioButtonPageLocators, \
    WebTablePageLocators, ButtonsPageLocators
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_all_fields(self):
        person_info = next(generated_person())
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address
        self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        self.driver.execute_script("window.scrollTo(200, document.body.scrollHeight);")
        self.element_is_visible(self.locators.SUBMIT).click()
        return full_name, email, current_address, permanent_address

    def check_filled_form(self):
        full_name = self.element_is_present(self.locators.CREATED_FULL_NAME).text.split(':')[1]
        email = self.element_is_present(self.locators.CREATED_EMAIL).text.split(':')[1]
        current_address = self.element_is_present(self.locators.CREATED_CURRENT_ADDRESS).text.split(':')[1]
        permanent_address = self.element_is_present(self.locators.CREATED_PERMANENT_ADDRESS).text.split(':')[1]
        return full_name, email, current_address, permanent_address


class CheckBoxPage(BasePage):
    locators = CheckBoxPageLocators()

    def open_full_list(self):
        self.element_is_visible(self.locators.EXPAND_ALL_BUTTON).click()

    def click_random_checkbox(self):
        items_list = self.elements_are_visible(self.locators.ITEM_LIST)
        count = 21
        while count > 0:
            item = choice(items_list)
            self.go_to_element(item)
            item.click()
            count -= 1

    def get_checked_checkboxes(self):
        checked_list = self.elements_are_present(self.locators.CHECKED_ITEMS)
        data = []
        for box in checked_list:
            title_item = box.find_element(*self.locators.TITLE_ITEM)
            data.append(title_item.text)
        return ' '.join([str(i).replace(' ', '').lower().split('.')[0] for i in data])

    def get_output_result(self):
        result_list = self.elements_are_present(self.locators.OUTPUT_RESULT)
        data = []
        for item in result_list:
            data.append(item.text)
        return ' '.join([i.lower() for i in data])


class RadioButtonPage(BasePage):
    locators = RadioButtonPageLocators()

    def click_radio_button(self, radio_choice):
        radio_choices = {"yes": self.locators.YES_RADIO,
                         "impressive": self.locators.IMPRESSIVE_RADIO,
                         "no": self.locators.NO_RADIO}
        self.element_is_visible(radio_choices[radio_choice]).click()

    def get_output_result(self):
        result = self.element_is_present(self.locators.TEXT_SUCCESS)
        return result.text


class WebTablePage(BasePage):
    locators = WebTablePageLocators()
    person_info = next(generated_person())

    def add_new_person(self):
        count = 1
        while count != 0:
            first_name = self.person_info.first_name
            last_name = self.person_info.last_name
            email = self.person_info.email
            age = self.person_info.age
            salary = self.person_info.salary
            department = self.person_info.department

            self.element_is_visible(self.locators.ADD_BUTTON).click()
            self.element_is_visible(self.locators.FIRST_NAME_INPUT).send_keys(first_name)
            self.element_is_visible(self.locators.LAST_NAME_INPUT).send_keys(last_name)
            self.element_is_visible(self.locators.EMAIL_INPUT).send_keys(email)
            self.element_is_visible(self.locators.AGE_INPUT).send_keys(age)
            self.element_is_visible(self.locators.SALARY_INPUT).send_keys(salary)
            self.element_is_visible(self.locators.DEPARTMENT_INPUT).send_keys(department)
            self.element_is_visible(self.locators.SUBMIT).click()

            count -= 1
            return [str(i) for i in [first_name, last_name, age, email, salary, department]]

    def check_added_person(self):
        full_person_list = self.elements_are_present(self.locators.FULL_PERSON_LIST)
        data = []
        for item in full_person_list:
            data.append(item.text.splitlines())
        return data

    def search_some_person(self, key_word):
        self.element_is_visible(self.locators.SEARCH_INPUT).send_keys(key_word)

    def check_search_person(self):
        delete_button = self.element_is_present(self.locators.DELETE_BUTTON)
        row = delete_button.find_element(*self.locators.ROW_PARENT)
        return row.text.splitlines()

    def update_person_info_first_name(self):
        first_name = self.person_info.first_name
        self.element_is_visible(self.locators.UPDATE_BUTTON).click()
        self.element_is_visible(self.locators.FIRST_NAME_INPUT).clear()
        self.element_is_visible(self.locators.FIRST_NAME_INPUT).send_keys(first_name)
        self.element_is_visible(self.locators.SUBMIT).click()
        return str(first_name)

    def update_person_info_last_name(self):
        last_name = self.person_info.last_name
        self.element_is_visible(self.locators.UPDATE_BUTTON).click()
        self.element_is_visible(self.locators.LAST_NAME_INPUT).clear()
        self.element_is_visible(self.locators.LAST_NAME_INPUT).send_keys(last_name)
        self.element_is_visible(self.locators.SUBMIT).click()
        return str(last_name)

    def update_person_info_email(self):
        email = self.person_info.email
        self.element_is_visible(self.locators.UPDATE_BUTTON).click()
        self.element_is_visible(self.locators.EMAIL_INPUT).clear()
        self.element_is_visible(self.locators.EMAIL_INPUT).send_keys(email)
        self.element_is_visible(self.locators.SUBMIT).click()
        return str(email)

    def delete_person(self):
        self.element_is_visible(self.locators.DELETE_BUTTON).click()

    def check_deleted_person(self):
        return self.element_is_present(self.locators.NO_ROWS_FOUND).text

    def select_up_to_some_rows(self):
        count = [5, 10, 20, 25, 50, 100]
        data = []
        self.remove_footer()
        self.remove_fixedban()
        for i in count:
            page_size_option_button = self.element_is_present(self.locators.PAGE_SIZE_OPTION)
            self.go_to_element(page_size_option_button)
            page_size_option_button.click()
            self.element_is_visible((By.CSS_SELECTOR, f"select option[value='{i}']")).click()
            data.append(self.check_changed_count_rows())
        return data

    def check_changed_count_rows(self):
        rows = self.elements_are_present(self.locators.FULL_PERSON_LIST)
        return len(rows)


class ButtonsPage(BasePage):
    locators = ButtonsPageLocators()

    def click_double_click_button(self):
        self.action_double_click(self.element_is_visible(self.locators.DOUBLE_CLICK_BUTTON))

    def click_right_click_button(self):
        self.action_right_click(self.element_is_visible(self.locators.RIGHT_CLICK_BUTTON))

    def click_click_me_button(self):
        self.element_is_visible(self.locators.CLICK_ME_BUTTON).click()

    def check_double_click_message(self):
        return self.element_is_visible(self.locators.DOUBLE_CLICK_MESSAGE).text

    def check_right_click_message(self):
        return self.element_is_visible(self.locators.RIGHT_CLICK_MESSAGE).text

    def check_click_me_message(self):
        return self.element_is_visible(self.locators.CLICK_ME_MESSAGE).text
