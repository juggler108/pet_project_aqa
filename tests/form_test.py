from time import sleep

import pytest

from pages.form_page import FormPage


class TestForm:
    class TestFormPage:
        @pytest.mark.xfail
        def test_form(self, driver):
            form_page = FormPage(driver, "https://demoqa.com/automation-practice-form")
            form_page.open()
            person_info = form_page.fill_all_form_fields()
            table_result = ' '.join(form_page.get_table_result()[:2]).split()
            assert person_info == table_result, "input and result do not match"
