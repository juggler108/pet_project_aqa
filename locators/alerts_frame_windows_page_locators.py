from selenium.webdriver.common.by import By


class BrowserWindowsPageLocators:
    NEW_TAB_BUTTON = (By.CSS_SELECTOR, "#tabButton")
    NEW_TAB_WINDOW_MESSAGE = (By.CSS_SELECTOR, "#sampleHeading")
    NEW_WINDOW_BUTTON = (By.CSS_SELECTOR, "#windowButton")


class AlertsPageLocators:
    ALERT_BUTTON = (By.CSS_SELECTOR, "#alertButton")
    CONFIRM_BUTTON = (By.CSS_SELECTOR, "#confirmButton")
    PROMPT_BUTTON = (By.CSS_SELECTOR, "#promtButton")

    # result
    TIMER_ALERT_BUTTON = (By.CSS_SELECTOR, "#timerAlertButton")
    CONFIRM_RESULT = (By.CSS_SELECTOR, "#confirmResult")
    PROMPT_RESULT = (By.CSS_SELECTOR, "#promptResult")
