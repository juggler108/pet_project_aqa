from random import choice, sample, randint
from time import sleep
import allure
from selenium.webdriver.support.select import Select
from generator.generator import generated_color, generated_date
from selenium.common import TimeoutException, ElementClickInterceptedException
from selenium.webdriver import Keys
from locators.widget_page_locators import AccordianPageLocators, AutoCompletePageLocators, DatePickerPageLocators, \
    SliderPageLocators, ProgressBarPageLocators, TabsPageLocators, ToolTipsPageLocators, MenuPageLocators
from pages.base_page import BasePage
from string import ascii_letters


class AccordianPage(BasePage):
    locators = AccordianPageLocators()

    @allure.step('check accordian widget')
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

    @allure.step('fill multi autocomplete input')
    def fill_input_multiple_color_names(self):
        colors = sample(next(generated_color()).color_name, k=randint(2, 5))
        for color in colors:
            input_multiple = self.element_is_clickable(self.locators.MULTIPLE_AUTO_COMPLETE_INPUT)
            input_multiple.send_keys(color)
            input_multiple.send_keys(Keys.ENTER)
        return colors

    @allure.step('remove value from multi autocomplete')
    def remove_value_from_multiple(self):
        count_value_before = len(self.elements_are_present(self.locators.MULTIPLE_VALUE))
        remove_button_lst = self.elements_are_present(self.locators.MULTIPLE_REMOVE_BUTTON)
        for remove_button in remove_button_lst:
            remove_button.click()
            break
        count_value_after = len(self.elements_are_present(self.locators.MULTIPLE_VALUE))
        return count_value_before, count_value_after

    @allure.step('check colors in multi autocomplete')
    def check_colors_multiple(self):
        colors = self.elements_are_present(self.locators.MULTIPLE_VALUE)
        colors_lst = []
        for color in colors:
            colors_lst.append(color.text)
        return colors_lst

    @allure.step('check button to remove all elements')
    def check_remove_all_button(self):
        self.element_is_visible(self.locators.MULTIPLE_REMOVE_ALL_BUTTON).click()
        try:
            return self.elements_are_visible(self.locators.MULTIPLE_VALUE)
        except TimeoutException:
            return []

    @allure.step('fill single autocomplete input')
    def fill_input_single_color_name(self):
        color = choice(next(generated_color()).color_name)
        input_single = self.element_is_clickable(self.locators.SINGLE_AUTO_COMPLETE_INPUT)
        input_single.send_keys(color)
        input_single.send_keys(Keys.ENTER)
        return color

    @allure.step('check color in single autocomplete')
    def check_color_single(self):
        color = self.element_is_visible(self.locators.SINGLE_VALUE)
        return color.text


class DatePickerPage(BasePage):
    locators = DatePickerPageLocators()

    @allure.step('change date')
    def check_select_date(self):
        date = next(generated_date())
        input_date = self.element_is_visible(self.locators.DATE_INPUT)
        value_date_before = input_date.get_attribute("value")
        input_date.click()
        self.set_date_by_text(self.locators.DATE_SELECT_MONTH, date.month)
        self.set_date_by_text(self.locators.DATE_SELECT_YEAR, date.year)
        self.set_date_item_from_list(self.locators.DATE_SELECT_DAY_LIST, date.day)
        value_date_after = input_date.get_attribute("value")
        return value_date_before, value_date_after

    @allure.step('change select date and time')
    def check_select_date_and_time(self):
        date = next(generated_date())
        input_date = self.element_is_visible(self.locators.DATE_AND_TIME_INPUT)
        value_date_before = input_date.get_attribute("value")
        input_date.click()
        self.element_is_visible(self.locators.DATE_AND_TIME_MONTH).click()
        self.set_date_item_from_list(self.locators.DATE_AND_TIME_MONTH_LIST, date.month)
        self.element_is_visible(self.locators.DATE_AND_TIME_YEAR).click()
        self.set_date_item_from_list(self.locators.DATE_AND_TIME_YEAR_LIST, "2020")
        self.set_date_item_from_list(self.locators.DATE_SELECT_DAY_LIST, date.day)
        self.set_date_item_from_list(self.locators.DATE_AND_TIME_TIME_LIST, date.time)
        input_date_after = self.element_is_visible(self.locators.DATE_AND_TIME_INPUT)
        value_date_after = input_date_after.get_attribute("value")
        return value_date_before, value_date_after

    @allure.step('select date by text')
    def set_date_by_text(self, element, value):
        select = Select(self.element_is_present(element))
        select.select_by_visible_text(value)

    @allure.step('select date item from list')
    def set_date_item_from_list(self, elements, value):
        item_list = self.elements_are_present(elements)
        for item in item_list:
            if item.text == value:
                item.click()
                break


class SliderPage(BasePage):
    locators = SliderPageLocators()

    @allure.step('change slider value')
    def change_slider_value(self):
        slider_value_before = self.element_is_present(self.locators.SLIDER_VALUE).get_attribute("value")
        self.action_drag_and_drop_by_offset(self.element_is_visible(self.locators.INPUT_SLIDER_VALUE), randint(0, 100), 0)
        slider_value_after = self.element_is_present(self.locators.SLIDER_VALUE).get_attribute("value")
        return slider_value_before, slider_value_after


class ProgressBarPage(BasePage):
    locators = ProgressBarPageLocators()

    @allure.step('change progress bar value')
    def change_progress_bar_value(self):
        progress_bar_value_before = self.element_is_present(self.locators.PROGRESS_BAR).get_attribute("aria-valuenow")
        self.element_is_clickable(self.locators.START_STOP_BUTTON).click()
        sleep(randint(1, 10))
        self.element_is_clickable(self.locators.START_STOP_BUTTON).click()
        progress_bar_value_after = self.element_is_present(self.locators.PROGRESS_BAR).get_attribute("aria-valuenow")
        return progress_bar_value_before, progress_bar_value_after

    @allure.step('check progress bar reset button')
    def reset_progress_bar_value(self):
        progress_bar_value_before = self.element_is_present(self.locators.PROGRESS_BAR).get_attribute("aria-valuenow")
        self.element_is_clickable(self.locators.START_STOP_BUTTON).click()
        self.element_is_clickable(self.locators.RESET_BUTTON, timeout=20).click()
        progress_bar_value_after = self.element_is_present(self.locators.PROGRESS_BAR).get_attribute("aria-valuenow")
        return progress_bar_value_before, progress_bar_value_after


class TabsPage(BasePage):
    locators = TabsPageLocators()

    @allure.step('check tabs')
    def check_tabs(self, name_tab):
        tabs = {
            "What":
                {"title": self.locators.TAB_WHAT,
                 "content": self.locators.TAB_WHAT_CONTENT},
            "Origin":
                {"title": self.locators.TAB_ORIGIN,
                 "content": self.locators.TAB_ORIGIN_CONTENT},
            "Use":
                {"title": self.locators.TAB_USE,
                 "content": self.locators.TAB_USE_CONTENT},
            "More":
                {"title": self.locators.TAB_MORE,
                 "content": self.locators.TAB_MORE_CONTENT},
        }
        button = self.element_is_visible(tabs[name_tab]["title"])
        button.click()
        content = self.element_is_present(tabs[name_tab]["content"])
        return button.text, len(content.text)


class ToolTipsPage(BasePage):
    locators = ToolTipsPageLocators()

    @allure.step('get text from tool tip')
    def get_text_from_tool_tips(self, hover_element):
        element = self.element_is_present(hover_element)
        self.action_move_to_element(element)
        sleep(0.5)
        tool_tip_text = self.element_is_visible(self.locators.TOOL_TIPS_INNERS).text
        return tool_tip_text

    @allure.step('check tool tip')
    def check_tool_tips(self):
        tool_tip_button = self.get_text_from_tool_tips(self.locators.HOVER_ME_BUTTON)
        tool_tip_field = self.get_text_from_tool_tips(self.locators.HOVER_ME_FIELD)
        tool_tip_contrary = self.get_text_from_tool_tips(self.locators.CONTRARY_LINK)
        tool_tip_section = self.get_text_from_tool_tips(self.locators.SECTION_LINK)
        return tool_tip_button, tool_tip_field, tool_tip_contrary, tool_tip_section


class MenuPage(BasePage):
    locators = MenuPageLocators()

    @allure.step('check menu item')
    def check_menu_items(self):
        values = ascii_letters + " 1234567890"
        menu_item_list = self.elements_are_present(self.locators.ITEM_LIST)
        data = []
        for item in menu_item_list:
            self.action_move_to_element(item)
            data.append(''.join([i for i in item.text if i in values]))
        return data
