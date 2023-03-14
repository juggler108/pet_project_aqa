import allure
import pytest
from pages.widgets_page import AccordianPage, AutoCompletePage, DatePickerPage, SliderPage, ProgressBarPage, TabsPage, \
    ToolTipsPage, MenuPage


@allure.suite('Widgets')
class TestWidgets:

    @allure.feature('Accordian Page')
    class TestAccordianPage:

        @allure.title('Check accordian widget')
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

    @allure.feature('Autocomplete page')
    class TestAutoCompletePage:

        @allure.title('Check the multi autocomplete is filled')
        def test_fill_multiple_auto_complete(self, driver):
            auto_complete_page = AutoCompletePage(driver, "https://demoqa.com/auto-complete")
            auto_complete_page.open()
            colors = auto_complete_page.fill_input_multiple_color_names()
            colors_result = auto_complete_page.check_colors_multiple()
            assert colors == colors_result, "added colors are missing in input field"

        @allure.title('Check delete from the multi autocomplete')
        def test_remove_autocomplete(self, driver):
            auto_complete_page = AutoCompletePage(driver, "https://demoqa.com/auto-complete")
            auto_complete_page.open()
            auto_complete_page.fill_input_multiple_color_names()
            count_value_before, count_value_after = auto_complete_page.remove_value_from_multiple()
            assert count_value_before == count_value_after + 1, "value has not been removed"

        @allure.title('Check button to remove all values the multi autocomplete')
        def test_remove_all_button(self, driver):
            auto_complete_page = AutoCompletePage(driver, "https://demoqa.com/auto-complete")
            auto_complete_page.open()
            auto_complete_page.fill_input_multiple_color_names()
            colors_after_remove_button = auto_complete_page.check_remove_all_button()
            assert len(colors_after_remove_button) == 0, "values have not been removed"

        @allure.title('Check the single autocomplete is filled')
        def test_fill_single_auto_complete(self, driver):
            auto_complete_page = AutoCompletePage(driver, "https://demoqa.com/auto-complete")
            auto_complete_page.open()
            color = auto_complete_page.fill_input_single_color_name()
            color_result = auto_complete_page.check_color_single()
            assert color == color_result, "added color is missing in input field"

    @allure.feature('Date Picker Page')
    class TestDatePickerPage:

        @allure.title('Check change date')
        def test_change_date(self, driver):
            date_picker_page = DatePickerPage(driver, "https://demoqa.com/date-picker")
            date_picker_page.open()
            value_date_before, value_date_after = date_picker_page.check_select_date()
            assert value_date_before != value_date_after, "the date has not been changed"

        @allure.title('Check change date and time')
        def test_change_date_and_time(self, driver):
            date_picker_page = DatePickerPage(driver, "https://demoqa.com/date-picker")
            date_picker_page.open()
            value_date_before, value_date_after = date_picker_page.check_select_date_and_time()
            assert value_date_before != value_date_after, "the date and time hava not been changed"

    @allure.feature('Slider Page')
    class TestSliderPage:

        @allure.title('Check moved slider')
        def test_slider(self, driver):
            slider_page = SliderPage(driver, "https://demoqa.com/slider")
            slider_page.open()
            slider_value_before, slider_value_after = slider_page.change_slider_value()
            assert slider_value_before != slider_value_after, "slider has not been moved"

    @allure.feature('Progress Bar Page')
    class TestProgressBarPage:

        @allure.title('Check changed progress bar')
        def test_progress_bar_start_stop(self, driver):
            progress_bar_page = ProgressBarPage(driver, "https://demoqa.com/progress-bar")
            progress_bar_page.open()
            progress_bar_value_before, progress_bar_value_after = progress_bar_page.change_progress_bar_value()
            assert progress_bar_value_before != progress_bar_value_after, "the progress bar value has not been changed"

        @allure.title('Check progress bar reset button')
        def test_progres_bar_reset(self, driver):
            progress_bar_page = ProgressBarPage(driver, "https://demoqa.com/progress-bar")
            progress_bar_page.open()
            progress_bar_value_before, progress_bar_value_after = progress_bar_page.reset_progress_bar_value()
            assert progress_bar_value_before == progress_bar_value_after, "reset_button did not reset value"

    @allure.feature('Test Tabs Page')
    class TestTabsPage:

        @allure.title('Check switched tabs')
        @pytest.mark.parametrize('name_tab', ["What", "Origin", "Use", "More"])
        def test_tabs(self, driver, name_tab):
            tabs_page = TabsPage(driver, "https://demoqa.com/tabs")
            tabs_page.open()
            button_text, len_content = tabs_page.check_tabs(name_tab=name_tab)
            assert button_text == name_tab and len_content > 0, f"the tab {name_tab} was not pressed or text is missing"

    @allure.feature('Tool Tips')
    class TestToolTipsPage:

        @allure.title('Check tool tips ')
        def test_tool_tips(self, driver):
            tool_tips_page = ToolTipsPage(driver, "https://demoqa.com/tool-tips")
            tool_tips_page.open()
            tool_tip_button, tool_tip_field, tool_tip_contrary, tool_tip_section = tool_tips_page.check_tool_tips()
            assert tool_tip_button == "You hovered over the Button", "hover element missing or incorrect content"
            assert tool_tip_field == "You hovered over the text field", "hover element missing or incorrect content"
            assert tool_tip_contrary == "You hovered over the Contrary", "hover element missing or incorrect content"
            assert tool_tip_section == "You hovered over the 1.10.32", "hover element missing or incorrect content"

    @allure.feature('Menu Page')
    class TestMenuPage:

        @allure.title('Check all of the menu items')
        def test_menu_items(self, driver):
            menu_page = MenuPage(driver, "https://demoqa.com/menu#")
            menu_page.open()
            items = ['Main Item 1', 'Main Item 2', 'Sub Item', 'Sub Item', 'SUB SUB LIST ', 'Sub Sub Item 1', 'Sub Sub Item 2', 'Main Item 3']
            item_list = menu_page.check_menu_items()
            assert item_list == items, "menu items does not exist or have not been selected"
