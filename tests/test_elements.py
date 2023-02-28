from pages.elements_page import TextBoxPage
from time import sleep


class TestElements:
    class TestTextBox:
        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, "https://demoqa.com/text-box")
            text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            output_name, output_email, output_cur_address, output_per_address = text_box_page.check_filled_form()
            assert full_name == output_name, "full name does not match"
            assert email == output_email, "email does not match"
            assert current_address.replace('\n', ' ') == output_cur_address, "current_address does not match"
            assert permanent_address.replace('\n', ' ') == output_per_address, "permanent_address does not match"
