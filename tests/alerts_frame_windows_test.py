from time import sleep

from pages.alerts_frame_windows_page import BrowserWindowsPage


class TestAlertsFrameWindows:
    class TestBrowserWindows:

        def test_new_window(self, driver):
            browser_windows_page = BrowserWindowsPage(driver, "https://demoqa.com/browser-windows")
            browser_windows_page.open()
            new_window_title = browser_windows_page.check_opened_new_window()
            assert new_window_title == "This is a sample page", "new window was not opened"


