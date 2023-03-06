from time import sleep

from pages.alerts_frame_windows_page import BrowserWindowsPage, AlertsPage


class TestAlertsFrameWindows:
    class TestBrowserWindows:

        def test_new_window(self, driver):
            browser_windows_page = BrowserWindowsPage(driver, "https://demoqa.com/browser-windows")
            browser_windows_page.open()
            new_window_title = browser_windows_page.check_opened_new_window()
            assert new_window_title == "This is a sample page", "new window was not opened"

    class TestAlerts:

        def test_click_button_to_see_alert(self, driver):
            alerts_page = AlertsPage(driver, "https://demoqa.com/alerts")
            alerts_page.open()
            alert_text = alerts_page.check_button_to_see_alert()
            assert alert_text == "You clicked a button", "alert did not show up"

        def test_alert_appear_after_5_sec(self, driver):
            alerts_page = AlertsPage(driver, "https://demoqa.com/alerts")
            alerts_page.open()
            alert_text = alerts_page.check_button_alert_appear_after_5_sec()
            assert alert_text == "This alert appeared after 5 seconds", "alert did not show up"

        def test_confirm_box_appear(self, driver):
            alerts_page = AlertsPage(driver, "https://demoqa.com/alerts")
            alerts_page.open()
            result_text = alerts_page.check_confirm_button()
            assert result_text == "You selected Ok", "alert did not show up"

        def test_prompt_box_appear(self, driver):
            alerts_page = AlertsPage(driver, "https://demoqa.com/alerts")
            alerts_page.open()
            entered_text, result_text = alerts_page.check_prompt_button()
            assert result_text == f"You entered {entered_text}", "alert did not show up"
