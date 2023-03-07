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


class FramesPageLocators:
    FIRST_FRAME = (By.CSS_SELECTOR, "#frame1")
    SECOND_FRAME = (By.CSS_SELECTOR, "#frame2")
    FRAME_TITLE = (By.CSS_SELECTOR, "#sampleHeading")


class NestedFramesPageLocators:
    PARENT_FRAME = (By.CSS_SELECTOR, "#frame1")
    PARENT_TEXT = (By.CSS_SELECTOR, "body")
    CHILD_FRAME = (By.CSS_SELECTOR, "iframe[srcdoc='<p>Child Iframe</p>']")
    CHILD_TEXT = (By.CSS_SELECTOR, "body > p")


class ModalDialogsPageLocators:
    SMALL_MODAL_BUTTON = (By.CSS_SELECTOR, "#showSmallModal")
    SMALL_MODAL_TITLE = (By.CSS_SELECTOR, "#example-modal-sizes-title-sm")
    CLOSE_SMALL_MODAL_BUTTON = (By.CSS_SELECTOR, "#closeSmallModal")
    LARGE_MODAL_BUTTON = (By.CSS_SELECTOR, "#showLargeModal")
    LARGE_MODAL_TITLE = (By.CSS_SELECTOR, "#example-modal-sizes-title-lg")
    CLOSE_LARGE_MODAL_BUTTON = (By.CSS_SELECTOR, "#closeLargeModal")
    MODAL_WINDOW = (By.CSS_SELECTOR, ".modal-content")
    MODAL_BODY = (By.CSS_SELECTOR, ".modal-body")

