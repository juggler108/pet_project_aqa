from time import sleep

from pages.widgets_page import AccordianPage, AutoCompletePage, DatePickerPage


class TestWidgets:
    class TestAccordianPage:
        def test_accordian(self, driver):
            accordian_page = AccordianPage(driver, "https://demoqa.com/accordian")
            accordian_page.open()
            first = accordian_page.check_accordian("first")
            second = accordian_page.check_accordian("second")
            third = accordian_page.check_accordian("third")
            assert first[0] == "What is Lorem Ipsum?", "the header of first accordian is not correct"
            assert len(first[1]) > 0, "there is no content of first accordian"
            assert second[0] == "Where does it come from?", "the header of second accordian is not correct"
            assert len(second[1]) > 0, "there is no content of second accordian"
            assert third[0] == "Why do we use it?", "the header of third accordian is not correct"
            assert len(third[1]) > 0, "there is no content of third accordian"

    class TestAutoCompletePage:
        def test_fill_multiple_auto_complete(self, driver):
            auto_complete_page = AutoCompletePage(driver, "https://demoqa.com/auto-complete")
            auto_complete_page.open()
            colors = auto_complete_page.fill_input_multiple_color_names()
            colors_result = auto_complete_page.check_colors_multiple()
            assert colors == colors_result, "added colors are missing in input field"

        def test_remove_autocomplete(self, driver):
            auto_complete_page = AutoCompletePage(driver, "https://demoqa.com/auto-complete")
            auto_complete_page.open()
            auto_complete_page.fill_input_multiple_color_names()
            count_value_before, count_value_after = auto_complete_page.remove_value_from_multiple()
            assert count_value_before == count_value_after + 1, "value has not been removed"

        def test_remove_all_button(self, driver):
            auto_complete_page = AutoCompletePage(driver, "https://demoqa.com/auto-complete")
            auto_complete_page.open()
            auto_complete_page.fill_input_multiple_color_names()
            colors_after_remove_button = auto_complete_page.check_remove_all_button()
            assert len(colors_after_remove_button) == 0, "values have not been removed"

        def test_fill_single_auto_complete(self, driver):
            auto_complete_page = AutoCompletePage(driver, "https://demoqa.com/auto-complete")
            auto_complete_page.open()
            color = auto_complete_page.fill_input_single_color_name()
            color_result = auto_complete_page.check_color_single()
            assert color == color_result, "added color is missing in input field"

    class TestDatePickerPage:
        def test_change_date(self, driver):
            date_picker_page = DatePickerPage(driver, "https://demoqa.com/date-picker")
            date_picker_page.open()
            value_date_before, value_date_after = date_picker_page.check_select_date()
            assert value_date_before != value_date_after, "the date has not been changed"

        def test_change_date_and_time(self, driver):
            date_picker_page = DatePickerPage(driver, "https://demoqa.com/date-picker")
            date_picker_page.open()
            value_date_before, value_date_after = date_picker_page.check_select_date_and_time()
            assert value_date_before != value_date_after, "the date and time hava not been changed"
