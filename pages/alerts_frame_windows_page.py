from random import choice

from locators.alerts_frame_windows_page_locators import BrowserWindowsPageLocators
from pages.base_page import BasePage


class BrowserWindowsPage(BasePage):
    locators = BrowserWindowsPageLocators()

    def check_opened_new_window(self):
        self.element_is_visible(choice([self.locators.NEW_TAB_BUTTON, self.locators.NEW_WINDOW_BUTTON])).click()
        self.switch_to_new_window()
        text = self.element_is_present(self.locators.NEW_TAB_WINDOW_MESSAGE).text
        return text
