from random import choice, sample, randint
from time import sleep
from generator.generator import generated_color
from selenium.common import TimeoutException
from selenium.webdriver import Keys
from locators.widget_page_locators import AccordianPageLocators, AutoCompletePageLocators
from pages.base_page import BasePage


class AccordianPage(BasePage):
    locators = AccordianPageLocators()

    def check_accordian(self, accordian):
        accordian_dict = {"first":
                              {"header": self.locators.SECTION_ONE_HEADER,
                               "text": self.locators.SECTION_ONE_TEXT},
                          "second":
                              {"header": self.locators.SECTION_TWO_HEADER,
                               "text": self.locators.SECTION_TWO_TEXT},
                          "third":
                              {"header": self.locators.SECTION_THREE_HEADER,
                               "text": self.locators.SECTION_THREE_TEXT}
                          }
        section_header = self.element_is_visible(accordian_dict[accordian]["header"])
        section_header.click()
        try:
            section_text = self.element_is_visible(accordian_dict[accordian]["text"]).text
        except TimeoutException:
            section_header.click()
            section_text = self.element_is_visible(accordian_dict[accordian]["text"]).text
        return [section_header.text, section_text]


class AutoCompletePage(BasePage):
    locators = AutoCompletePageLocators()

    def fill_input_multiple_color_names(self):
        colors = sample(next(generated_color()).color_name, k=randint(2, 5))
        for color in colors:
            input_multiple = self.element_is_clickable(self.locators.MULTIPLE_AUTO_COMPLETE_INPUT)
            input_multiple.send_keys(color)
            input_multiple.send_keys(Keys.ENTER)
        return colors

    def remove_value_from_multiple(self):
        count_value_before = len(self.elements_are_present(self.locators.MULTIPLE_VALUE))
        remove_button_lst = self.elements_are_present(self.locators.MULTIPLE_REMOVE_BUTTON)
        for remove_button in remove_button_lst:
            remove_button.click()
            break

        count_value_after = len(self.elements_are_present(self.locators.MULTIPLE_VALUE))
        return count_value_before, count_value_after

    def check_colors_multiple(self):
        colors = self.elements_are_present(self.locators.MULTIPLE_VALUE)
        colors_lst = []
        for color in colors:
            colors_lst.append(color.text)
        return colors_lst

    def check_remove_all_button(self):
        self.element_is_visible(self.locators.MULTIPLE_REMOVE_ALL_BUTTON).click()
        try:
            return self.elements_are_visible(self.locators.MULTIPLE_VALUE)
        except TimeoutException:
            return []

    def fill_input_single_color_name(self):
        color = choice(next(generated_color()).color_name)
        input_single = self.element_is_clickable(self.locators.SINGLE_AUTO_COMPLETE_INPUT)
        input_single.send_keys(color)
        input_single.send_keys(Keys.ENTER)
        return color

    def check_color_single(self):
        color = self.element_is_visible(self.locators.SINGLE_VALUE)
        return color.text
