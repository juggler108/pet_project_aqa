from random import choice
from time import sleep

from locators.alerts_frame_windows_page_locators import BrowserWindowsPageLocators, AlertsPageLocators
from pages.base_page import BasePage


class BrowserWindowsPage(BasePage):
    locators = BrowserWindowsPageLocators()

    def check_opened_new_window(self):
        self.element_is_visible(choice([self.locators.NEW_TAB_BUTTON, self.locators.NEW_WINDOW_BUTTON])).click()
        self.switch_to_new_window()
        text = self.element_is_present(self.locators.NEW_TAB_WINDOW_MESSAGE).text
        return text


class AlertsPage(BasePage):
    locators = AlertsPageLocators()

    def check_button_to_see_alert(self):
        self.element_is_visible(self.locators.ALERT_BUTTON).click()
        return self.switch_to_alert().text

    def check_button_alert_appear_after_5_sec(self):
        self.element_is_visible(self.locators.TIMER_ALERT_BUTTON).click()
        sleep(5)
        return self.switch_to_alert().text

    def check_confirm_button(self):
        self.element_is_visible(self.locators.CONFIRM_BUTTON).click()
        self.switch_to_alert().accept()
        result_text = self.element_is_visible(self.locators.CONFIRM_RESULT).text
        return result_text

    def check_prompt_button(self):
        self.element_is_visible(self.locators.PROMPT_BUTTON).click()
        entered_text = "qwerty"
        self.switch_to_alert().send_keys(entered_text)
        self.switch_to_alert().accept()
        result_text = self.element_is_visible(self.locators.PROMPT_RESULT).text
        return entered_text, result_text
