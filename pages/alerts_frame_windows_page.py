from random import choice
from time import sleep

from locators.alerts_frame_windows_page_locators import BrowserWindowsPageLocators, AlertsPageLocators, \
    FramesPageLocators, NestedFramesPageLocators
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


class FramesPage(BasePage):
    locators = FramesPageLocators()

    def check_frame(self, frame_num):
        if frame_num == "frame1":
            frame = self.element_is_visible(self.locators.FIRST_FRAME)
            width = frame.get_attribute("width")
            height = frame.get_attribute("height")
            self.switch_to_frame(frame)
            text = self.element_is_present(self.locators.FRAME_TITLE).text
            self.switch_to_default_content()
            return [text, width, height]
        if frame_num == "frame2":
            frame = self.element_is_visible(self.locators.SECOND_FRAME)
            width = frame.get_attribute("width")
            height = frame.get_attribute("height")
            self.switch_to_frame(frame)
            text = self.element_is_present(self.locators.FRAME_TITLE).text
            return [text, width, height]


class NestedFramesPage(BasePage):
    locators = NestedFramesPageLocators()

    def check_nested_frames(self):
        parent_frame = self.element_is_present(self.locators.PARENT_FRAME)
        self.switch_to_frame(parent_frame)
        parent_text = self.element_is_present(self.locators.PARENT_TEXT).text
        child_frame = self.element_is_present(self.locators.CHILD_FRAME)
        self.switch_to_frame(child_frame)
        child_text = self.element_is_present(self.locators.CHILD_TEXT).text
        return parent_text, child_text



