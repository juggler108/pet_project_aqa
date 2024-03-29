import random
import re
from time import sleep

import allure

from locators.interactions_page_locators import SortablePageLocators, SelectablePageLocators, ResizablePageLocators, \
    DroppablePageLocators, DraggablePageLocators
from pages.base_page import BasePage


class SortablePage(BasePage):
    locators = SortablePageLocators()

    @allure.step('get sortable items')
    def get_item_list(self, elements):
        return [item.text for item in self.elements_are_visible(elements)]

    @allure.step('change list order')
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

    @allure.step('change grid order')
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

    @allure.step('click selectable item')
    def click_selectable_item(self, elements):
        elements = self.elements_are_visible(elements)
        random.choice(elements).click()

    @allure.step('select list item')
    def select_list_item(self):
        self.element_is_visible(self.locators.TAB_LIST).click()
        self.click_selectable_item(self.locators.VERTICAL_ITEM_LIST)
        active_element = self.element_is_visible(self.locators.VERTICAL_LIST_ITEM__ACTIVE)
        return active_element.text

    @allure.step('select grid item')
    def select_grid_item(self):
        self.element_is_visible(self.locators.TAB_GRID).click()
        self.click_selectable_item(self.locators.GRID_ITEM_LIST)
        active_element = self.element_is_visible(self.locators.GRID_ITEM_ACTIVE)
        return active_element.text


class ResizablePage(BasePage):
    locators = ResizablePageLocators()

    @allure.step('get px from width and height')
    def get_width_and_height_pixels(self, value_of_size):
        width = value_of_size.split(";")[0].split(":")[1].strip()
        height = value_of_size.split(";")[1].split(":")[1].strip()
        return width, height

    @allure.step('get max and min size')
    def get_max_min_size(self, locator):
        size_value = self.element_is_present(locator).get_attribute("style")
        return size_value

    @allure.step('change size resizable box')
    def change_size_resizable_box(self):
        self.action_drag_and_drop_by_offset(self.element_is_present(self.locators.RESIZABLE_BOX_HANDLE), 400, 200)
        max_size = self.get_width_and_height_pixels(self.get_max_min_size(self.locators.RESIZABLE_BOX))
        self.action_drag_and_drop_by_offset(self.element_is_present(self.locators.RESIZABLE_BOX_HANDLE), -500, -300)
        min_size = self.get_width_and_height_pixels(self.get_max_min_size(self.locators.RESIZABLE_BOX))
        return max_size, min_size

    @allure.step('change size resizable')
    def change_size_resizable(self):
        self.action_drag_and_drop_by_offset(self.element_is_visible(
            self.locators.RESIZABLE_HANDLE), random.randint(1, 300), random.randint(1, 300))
        max_size = self.get_width_and_height_pixels(self.get_max_min_size(self.locators.RESIZABLE))
        self.action_drag_and_drop_by_offset(self.element_is_visible(
            self.locators.RESIZABLE_HANDLE), random.randint(-200, -3), random.randint(-200, -3))
        min_size = self.get_width_and_height_pixels(self.get_max_min_size(self.locators.RESIZABLE))
        return max_size, min_size


class DroppablePage(BasePage):
    locators = DroppablePageLocators()

    @allure.step('drop simple box')
    def check_simple_droppable(self):
        self.element_is_visible(self.locators.SIMPLE_TAB).click()
        drag_box = self.element_is_visible(self.locators.SIMPLE_DRAG_ME)
        drop_box = self.element_is_visible(self.locators.SIMPLE_DROPPED)
        self.action_drag_and_drop_to_element(drag_box, drop_box)
        return drop_box.text

    @allure.step('drop accept box')
    def check_accept_droppable(self):
        self.element_is_visible(self.locators.ACCEPT_TAB).click()
        drag_box_acceptable = self.element_is_visible(self.locators.ACCEPT_ACCEPTABLE)
        drag_box_not_acceptable = self.element_is_visible(self.locators.ACCEPT_NOT_ACCEPTABLE)
        drop_box = self.element_is_visible(self.locators.ACCEPT_DROPPABLE)
        self.action_drag_and_drop_to_element(drag_box_not_acceptable, drop_box)
        not_acceptable_text = self.element_is_present(self.locators.ACCEPT_DROPPABLE).text
        self.action_drag_and_drop_to_element(drag_box_acceptable, drop_box)
        acceptable_text = self.element_is_present(self.locators.ACCEPT_DROPPABLE).text
        return not_acceptable_text, acceptable_text

    @allure.step('drop prevent propogation box')
    def check_prevent_propogation_droppable(self):
        self.element_is_visible(self.locators.PREVENT_TAB).click()
        drag_box = self.element_is_visible(self.locators.PREVENT_DRAG_ME)
        not_greedy_inner = self.element_is_visible(self.locators.PREVENT_NOT_GREEDY_INNER_BOX)
        greedy_inner = self.element_is_visible(self.locators.PREVENT_GREEDY_INNER_BOX)
        self.action_drag_and_drop_to_element(drag_box, not_greedy_inner)
        text_not_greedy_outer = self.element_is_visible(self.locators.PREVENT_NOT_GREEDY_OUTER_BOX_TEXT).text
        text_not_greedy_inner = not_greedy_inner.text
        self.action_drag_and_drop_to_element(drag_box, greedy_inner)
        text_greedy_outer = self.element_is_visible(self.locators.PREVENT_GREEDY_OUTER_BOX_TEXT).text
        text_greedy_inner = greedy_inner.text
        return text_not_greedy_outer, text_not_greedy_inner, text_greedy_outer, text_greedy_inner

    @allure.step('drag revert draggable box')
    def check_revert_draggable(self, type_drag):
        drag_boxes = {"will_revert": self.locators.WILL_REVERT, "not_revert": self.locators.NOT_REVERT}
        self.element_is_visible(self.locators.REVERT_TAB).click()
        drag_box = self.element_is_visible(drag_boxes[type_drag])
        drop_here_box = self.element_is_visible(self.locators.REVERT_DROP_HERE)
        self.action_drag_and_drop_to_element(drag_box, drop_here_box)
        position_after_move = drag_box.get_attribute("style")
        sleep(1)
        position_after_revert = drag_box.get_attribute("style")
        return position_after_move, position_after_revert


class DraggablePage(BasePage):
    locators = DraggablePageLocators()

    @allure.step('get before and after positions')
    def get_before_and_after_position(self, drag_element):
        self.action_drag_and_drop_by_offset(drag_element, random.randint(0, 150), random.randint(0, 150))
        before_position = drag_element.get_attribute("style")
        sleep(0.2)
        self.action_drag_and_drop_by_offset(drag_element, random.randint(0, 150), random.randint(0, 150))
        after_position = drag_element.get_attribute("style")
        return before_position, after_position

    @allure.step('simple drag and drop')
    def check_simple_draggable(self):
        self.element_is_visible(self.locators.SIMPLE_TAB).click()
        drag_element = self.element_is_visible(self.locators.SIMPLE_DRAG_ME)
        before_position, after_position = self.get_before_and_after_position(drag_element=drag_element)
        return before_position, after_position

    @allure.step('get position before')
    def get_position_before(self, position):
        return re.findall(r"[0-9]+", position[0])

    @allure.step('get position after')
    def get_position_after(self, position):
        return re.findall(r"[0-9]+", position[1])

    @allure.step('drag only_x or only_y direction')
    def axis_restricted_x(self, drag_box):
        drag_boxes = {"only_x": self.locators.RESTRICTED_ONLY_X, "only_y": self.locators.RESTRICTED_ONLY_Y}
        self.element_is_visible(self.locators.RESTRICTED_TAB).click()
        box = self.element_is_visible(drag_boxes[drag_box])
        position = self.get_before_and_after_position(box)
        position_before, position_after = self.get_position_before(position), self.get_position_after(position)
        return position_before, position_after
