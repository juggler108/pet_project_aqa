from time import sleep

from selenium.common import TimeoutException

from locators.widget_page_locators import AccordianPageLocators
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
