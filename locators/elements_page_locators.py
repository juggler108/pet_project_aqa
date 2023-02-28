from selenium.webdriver.common.by import By


class TextBoxPageLocators:
    # Form fields
    FULL_NAME = (By.CSS_SELECTOR, "input#userName")
    EMAIL = (By.CSS_SELECTOR, "input[id='userEmail']")
    CURRENT_ADDRESS = (By.CSS_SELECTOR, "textarea#currentAddress")
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, "textarea#permanentAddress")
    SUBMIT = (By.CSS_SELECTOR, "#submit")

    # Created form
    CREATED_FULL_NAME = (By.CSS_SELECTOR, "#output #name")
    CREATED_EMAIL = (By.CSS_SELECTOR, "#output #email")
    CREATED_CURRENT_ADDRESS = (By.CSS_SELECTOR, "#output #currentAddress")
    CREATED_PERMANENT_ADDRESS = (By.CSS_SELECTOR, "#output #permanentAddress")


class CheckBoxPageLocators:
    EXPAND_ALL_BUTTON = (By.CSS_SELECTOR, "button[title='Expand all']")
    ITEM_LIST = (By.CSS_SELECTOR, "span.rct-title")
    CHECKED_ITEMS = (By.CSS_SELECTOR, "svg.rct-icon-check")
    TITLE_ITEM = (By.XPATH, ".//ancestor::span[@class='rct-text']")
    OUTPUT_RESULT = (By.CSS_SELECTOR, ".text-success")
