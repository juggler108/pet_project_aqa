from pages.widgets_page import AccordianPage


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
