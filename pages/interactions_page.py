import random

from locators.interactions_page_locators import SortablePageLocators, SelectablePageLocators
from pages.base_page import BasePage


class SortablePage(BasePage):
    locators = SortablePageLocators()

    def get_item_list(self, elements):
        return [item.text for item in self.elements_are_visible(elements)]

    def change_list_item_order(self):
        self.element_is_visible(self.locators.TAB_LIST).click()
        order_before = self.get_item_list(self.locators.VERTICAL_ITEM_LIST)
        item_list = self.elements_are_visible(self.locators.VERTICAL_ITEM_LIST)
        for _ in range(random.randint(1, 7)):
            item_what = item_list[random.randint(0, 5)]
            item_where = item_list[random.randint(0, 5)]
            self.action_drag_and_drop_to_element(item_what, item_where)
        order_after = self.get_item_list(self.locators.VERTICAL_ITEM_LIST)
        return order_before, order_after

    def change_grid_item_order(self):
        self.element_is_visible(self.locators.TAB_GRID).click()
        order_before = self.get_item_list(self.locators.GRID_ITEM_LIST)
        item_list = self.elements_are_visible(self.locators.GRID_ITEM_LIST)
        for _ in range(random.randint(1, 7)):
            item_what = item_list[random.randint(0, 8)]
            item_where = item_list[random.randint(0, 8)]
            self.action_drag_and_drop_to_element(item_what, item_where)
        order_after = self.get_item_list(self.locators.GRID_ITEM_LIST)
        return order_before, order_after


class SelectablePage(BasePage):
    locators = SelectablePageLocators()

    def click_selectable_item(self, elements):
        elements = self.elements_are_visible(elements)
        random.choice(elements).click()

    def select_list_item(self):
        self.element_is_visible(self.locators.TAB_LIST).click()
        self.click_selectable_item(self.locators.VERTICAL_ITEM_LIST)
        active_element = self.element_is_visible(self.locators.VERTICAL_LIST_ITEM__ACTIVE)
        return active_element.text

    def select_grid_item(self):
        self.element_is_visible(self.locators.TAB_GRID).click()
        self.click_selectable_item(self.locators.GRID_ITEM_LIST)
        active_element = self.element_is_visible(self.locators.GRID_ITEM_ACTIVE)
        return active_element.text
