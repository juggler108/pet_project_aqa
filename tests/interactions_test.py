from time import sleep

from pages.interactions_page import SortablePage, SelectablePage, ResizablePage


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

    class TestSelectablePage:
        def test_list_selectable_item(self, driver):
            selectable_page = SelectablePage(driver, "https://demoqa.com/selectable")
            selectable_page.open()
            active_element = selectable_page.select_list_item()
            assert active_element != 0, "no elements were selected"

        def test_grid_selectable_item(self, driver):
            selectable_page = SelectablePage(driver, "https://demoqa.com/selectable")
            selectable_page.open()
            active_element = selectable_page.select_grid_item()
            assert active_element != 0, "no elements were selected"

    class TestResizablePage:
        def test_resizable(self, driver):
            resizable_page = ResizablePage(driver, "https://demoqa.com/resizable")
            resizable_page.open()
            max_resize_box, min_resize_box = resizable_page.change_size_resizable_box()
            max_resize, min_resize = resizable_page.change_size_resizable()
            assert max_resize_box == ('500px', '300px'), "max size is not equal to 500x300 px"
            assert min_resize_box == ('150px', '150px'), "min size is not equal to 150x150 px"
            assert min_resize != max_resize, "resizable has not been changed"


