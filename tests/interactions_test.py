from time import sleep

from pages.interactions_page import SortablePage


class TestInteractions:
    class TestSortablePage:
        def test_list_sortable(self, driver):
            sortable_page = SortablePage(driver, "https://demoqa.com/sortable")
            sortable_page.open()
            order_before, order_after = sortable_page.change_list_item_order()
            assert order_before != order_after, "the order of list has not been changed"

        def test_grid_sortable(self, driver):
            sortable_page = SortablePage(driver, "https://demoqa.com/sortable")
            sortable_page.open()
            order_before, order_after = sortable_page.change_grid_item_order()
            assert order_before != order_after, "the order of grid has not been changed"
