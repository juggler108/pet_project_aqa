import allure
from pages.interactions_page import SortablePage, SelectablePage, ResizablePage, DroppablePage, DraggablePage


@allure.suite('Interactions')
class TestInteractions:

    @allure.feature('Sortable Page')
    class TestSortablePage:

        @allure.title('Check changed sortable list')
        def test_list_sortable(self, driver):
            sortable_page = SortablePage(driver, "https://demoqa.com/sortable")
            sortable_page.open()
            order_before, order_after = sortable_page.change_list_item_order()
            assert order_before != order_after, "the order of list has not been changed"

        @allure.title('Check changed sortable grid')
        def test_grid_sortable(self, driver):
            sortable_page = SortablePage(driver, "https://demoqa.com/sortable")
            sortable_page.open()
            order_before, order_after = sortable_page.change_grid_item_order()
            assert order_before != order_after, "the order of grid has not been changed"

    @allure.feature('Selectable Page')
    class TestSelectablePage:

        @allure.title('Check changed selectable list')
        def test_list_selectable_item(self, driver):
            selectable_page = SelectablePage(driver, "https://demoqa.com/selectable")
            selectable_page.open()
            active_element = selectable_page.select_list_item()
            assert active_element != 0, "no elements were selected"

        @allure.title('Check changed selectable grid')
        def test_grid_selectable_item(self, driver):
            selectable_page = SelectablePage(driver, "https://demoqa.com/selectable")
            selectable_page.open()
            active_element = selectable_page.select_grid_item()
            assert active_element != 0, "no elements were selected"

    @allure.feature('Resizable Page')
    class TestResizablePage:

        @allure.title('Check changed resizable boxes')
        def test_resizable(self, driver):
            resizable_page = ResizablePage(driver, "https://demoqa.com/resizable")
            resizable_page.open()
            max_resize_box, min_resize_box = resizable_page.change_size_resizable_box()
            max_resize, min_resize = resizable_page.change_size_resizable()
            assert max_resize_box == ('500px', '300px'), "max size is not equal to 500x300 px"
            assert min_resize_box == ('150px', '150px'), "min size is not equal to 150x150 px"
            assert min_resize != max_resize, "resizable has not been changed"

    @allure.feature('Droppable Page')
    class TestDroppablePage:

        @allure.title('Check simple droppable')
        def test_simple_droppable(self, driver):
            droppable_page = DroppablePage(driver, "https://demoqa.com/droppable")
            droppable_page.open()
            drop_box_text = droppable_page.check_simple_droppable()
            assert drop_box_text == "Dropped!", "the draggable element has not been dropped"

        @allure.title('Check accept droppable')
        def test_accept_droppable(self, driver):
            droppable_page = DroppablePage(driver, "https://demoqa.com/droppable")
            droppable_page.open()
            not_acceptable_text, acceptable_text = droppable_page.check_accept_droppable()
            assert not_acceptable_text == "Drop here", "the dropped 'not acceptable element' has been accepted"
            assert acceptable_text == "Dropped!", "the dropped 'acceptable element' has not been accepted"

        @allure.title('Check prevent propogation droppable')
        def test_prevent_propogation_droppable(self, driver):
            droppable_page = DroppablePage(driver, "https://demoqa.com/droppable")
            droppable_page.open()
            not_greedy, not_greedy_inner, greedy, greedy_inner = droppable_page.check_prevent_propogation_droppable()
            assert not_greedy == "Dropped!", "the 'not greedy element' text has not changed"
            assert not_greedy_inner == "Dropped!", "the 'not greedy element' text has not changed"
            assert greedy == "Outer droppable", "the 'greedy element' text has changed"
            assert greedy_inner == "Dropped!", "the 'greedy element' text has not changed"

        @allure.title('Check revert draggable droppable')
        def test_revert_draggable_droppable(self, driver):
            droppable_page = DroppablePage(driver, "https://demoqa.com/droppable")
            droppable_page.open()
            will_after_move, will_after_revert = droppable_page.check_revert_draggable("will_revert")
            not_revert_after_move, will_not_after_revert = droppable_page.check_revert_draggable("not_revert")
            assert will_after_move != will_after_revert, "the 'will revert' element has not reverted"
            assert not_revert_after_move == will_not_after_revert, "the 'will not revert' element has reverted"

    @allure.feature('Draggable Page')
    class TestDraggablePage:

        @allure.title('Check simple draggable')
        def test_simple_draggable(self, driver):
            draggable_page = DraggablePage(driver, "https://demoqa.com/dragabble")
            draggable_page.open()
            before_position, after_position = draggable_page.check_simple_draggable()
            assert before_position != after_position, "the position of the box has not changed"

        @allure.title('Check axis restricted draggable')
        def test_axis_restricted_draggable(self, driver):
            draggable_page = DraggablePage(driver, "https://demoqa.com/dragabble")
            draggable_page.open()
            position_x_before, position_x_after = draggable_page.axis_restricted_x('only_x')
            position_y_before, position_y_after = draggable_page.axis_restricted_x('only_y')
            assert position_x_before != position_x_after, "the only_x box position has not changed"
            assert position_x_before[1] == '0' and position_x_after[1] == '0', "only_x box position shifted in y_axis"
            assert position_y_before != position_y_after, "the only_y box position has not changed"
            assert position_y_before[0] == '0' and position_y_after[0] == '0', "only_y box position shifted in x_axis"
