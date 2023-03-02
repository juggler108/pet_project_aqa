from random import randint
import pytest
from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage, ButtonsPage, LinksPage, \
    UploadAndDownloadPage
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

    class TestCheckBox:
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, "https://demoqa.com/checkbox")
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            checked_checkboxes = check_box_page.get_checked_checkboxes()
            output_result = check_box_page.get_output_result()
            assert checked_checkboxes == output_result, "checkboxes have not been selected"

    class TestRadioButton:
        @pytest.mark.xfail
        def test_radio_button(self, driver):
            radio_button_page = RadioButtonPage(driver, "https://demoqa.com/radio-button")
            radio_button_page.open()
            radio_button_page.click_radio_button('yes')
            output_yes = radio_button_page.get_output_result()
            radio_button_page.click_radio_button('impressive')
            output_impressive = radio_button_page.get_output_result()
            radio_button_page.click_radio_button('no')
            output_no = radio_button_page.get_output_result()
            assert output_yes == 'Yes', "'Yes' radiobutton has not been selected"
            assert output_impressive == 'Impressive', "'Impressive' radiobutton has not been selected"
            assert output_no == 'No', "'No' radiobutton has not been selected"

    class TestWebTable:
        def test_web_table_add_person(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            new_person = web_table_page.add_new_person()
            table_result = web_table_page.check_added_person()
            assert new_person in table_result, "new person has not been added"

        def test_web_table_search_person(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            first_name = web_table_page.add_new_person()[0]
            web_table_page.search_some_person(first_name)
            table_result = web_table_page.check_search_person()
            assert first_name in table_result, "the person was not found in the table"

        def test_web_table_update_person_info_first_name(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            last_name = web_table_page.add_new_person()[0]
            web_table_page.search_some_person(last_name)
            update_info = web_table_page.update_person_info_first_name()
            update_row = web_table_page.check_search_person()
            assert update_info in update_row, "the person cart has not been changed"

        def test_web_table_update_person_info_last_name(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            last_name = web_table_page.add_new_person()[1]
            web_table_page.search_some_person(last_name)
            update_info = web_table_page.update_person_info_last_name()
            update_row = web_table_page.check_search_person()
            assert update_info in update_row, "the person cart has not been changed"

        def test_web_table_update_person_info_email(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            last_name = web_table_page.add_new_person()[3]
            web_table_page.search_some_person(last_name)
            update_info = web_table_page.update_person_info_email()
            update_row = web_table_page.check_search_person()
            assert update_info in update_row, "the person cart has not been changed"

        def test_web_table_delete_person(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            email = web_table_page.add_new_person()[3]
            web_table_page.search_some_person(email)
            web_table_page.delete_person()
            text = web_table_page.check_deleted_person()
            assert text == "No rows found", "the person has not been deleted"

        @pytest.mark.xfail
        def test_web_table_change_count_row(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            changed_count_rows = web_table_page.select_up_to_some_rows()
            assert changed_count_rows == [5, 10, 20, 25, 50, 100], \
                "the number of rows have not been changed or changed incorrectly"

    class TestButtonsPage:
        def test_buttons_page_double_click_button(self, driver):
            buttons_page = ButtonsPage(driver, "https://demoqa.com/buttons")
            buttons_page.open()
            buttons_page.click_double_click_button()
            message = buttons_page.check_double_click_message()
            assert message == "You have done a double click", "double click button was not pressed"

        def test_buttons_page_right_click_button(self, driver):
            buttons_page = ButtonsPage(driver, "https://demoqa.com/buttons")
            buttons_page.open()
            buttons_page.click_right_click_button()
            message = buttons_page.check_right_click_message()
            assert message == "You have done a right click", "right click button was not pressed"

        def test_buttons_page_click_me_button(self, driver):
            buttons_page = ButtonsPage(driver, "https://demoqa.com/buttons")
            buttons_page.open()
            buttons_page.click_click_me_button()
            message = buttons_page.check_click_me_message()
            assert message == "You have done a dynamic click", "click me button was not pressed"

    class TestLinksPage:
        def test_check_link(self, driver):
            links_page = LinksPage(driver, "https://demoqa.com/links")
            links_page.open()
            href_link, current_url = links_page.check_new_tab_simple_link()
            assert href_link == current_url, "the link is broken or url is incorrect"

        def test_broken_link(self, driver):
            links_page = LinksPage(driver, "https://demoqa.com/links")
            links_page.open()
            response_code = links_page.check_bad_request_link("https://demoqa.com/bad-request")
            assert response_code == 400, "the link works or the status code is not 400"

        def test_no_content_link(self, driver):
            links_page = LinksPage(driver, "https://demoqa.com/links")
            links_page.open()
            response_code = links_page.check_no_content_link("https://demoqa.com/no-content")
            assert response_code == 204, "the link works or the status code is not 204"

    class TestUploadAndDownload:
        def test_upload_file(self, driver):
            upload_and_download_page = UploadAndDownloadPage(driver, "https://demoqa.com/upload-download")
            upload_and_download_page.open()
            path, uploaded_file = upload_and_download_page.upload_file()
            assert path == uploaded_file, "the file has not been uploaded"

        def test_download_file(self, driver):
            upload_and_download_page = UploadAndDownloadPage(driver, "https://demoqa.com/upload-download")
            upload_and_download_page.open()
            check = upload_and_download_page.download_file()
            assert check is True, "the file has not been downloaded"
