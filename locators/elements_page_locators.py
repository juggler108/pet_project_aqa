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


class RadioButtonPageLocators:
    YES_RADIO = (By.CSS_SELECTOR, "label[for='yesRadio']")
    IMPRESSIVE_RADIO = (By.CSS_SELECTOR, "label[for='impressiveRadio']")
    NO_RADIO = (By.CSS_SELECTOR, "label[for='noRadio']")
    TEXT_SUCCESS = (By.CSS_SELECTOR, ".text-success")


class WebTablePageLocators:
    # add person form
    ADD_BUTTON = (By.CSS_SELECTOR, "#addNewRecordButton")
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, "#firstName")
    LAST_NAME_INPUT = (By.CSS_SELECTOR, "#lastName")
    EMAIL_INPUT = (By.CSS_SELECTOR, "#userEmail")
    AGE_INPUT = (By.CSS_SELECTOR, "#age")
    SALARY_INPUT = (By.CSS_SELECTOR, "#salary")
    DEPARTMENT_INPUT = (By.CSS_SELECTOR, "#department")
    SUBMIT = (By.CSS_SELECTOR, "#submit")

    # tables
    FULL_PERSON_LIST = (By.CSS_SELECTOR, "div.rt-tr-group")
    SEARCH_INPUT = (By.CSS_SELECTOR, "#searchBox")
    DELETE_BUTTON = (By.CSS_SELECTOR, "span[title='Delete']")
    ROW_PARENT = (By.XPATH, ".//ancestor::div[@class='rt-tr-group']")
    NO_ROWS_FOUND = (By.CSS_SELECTOR, ".rt-noData")
    PAGE_SIZE_OPTION = (By.CSS_SELECTOR, ".select-wrap")

    # update
    UPDATE_BUTTON = (By.CSS_SELECTOR, "span[title='Edit']")


class ButtonsPageLocators:
    # buttons
    DOUBLE_CLICK_BUTTON = (By.CSS_SELECTOR, "#doubleClickBtn")
    RIGHT_CLICK_BUTTON = (By.CSS_SELECTOR, "#rightClickBtn")
    CLICK_ME_BUTTON = (By.XPATH, "//div[3]/button")

    # results
    DOUBLE_CLICK_MESSAGE = (By.CSS_SELECTOR, "#doubleClickMessage")
    RIGHT_CLICK_MESSAGE = (By.CSS_SELECTOR, "#rightClickMessage")
    CLICK_ME_MESSAGE = (By.CSS_SELECTOR, "#dynamicClickMessage")


class LinksPageLocators:
    SIMPLE_LINK = (By.CSS_SELECTOR, "#simpleLink")
    NO_CONTENT = (By.CSS_SELECTOR, "#no-content")
    BAD_REQUEST = (By.CSS_SELECTOR, "#bad-request")


class UploadAndDownloadLocators:
    UPLOAD_FILE = (By.CSS_SELECTOR, "#uploadFile")
    DOWNLOAD_FILE = (By.CSS_SELECTOR, "#downloadButton")

    UPLOADED_RESULT = (By.CSS_SELECTOR, "#uploadedFilePath")


class DynamicPropertiesLocators:
    ENABLE_AFTER_BUTTON = (By.CSS_SELECTOR, "#enableAfter")
    COLOR_CHANGE_BUTTON = (By.CSS_SELECTOR, "#colorChange")
    VISIBLE_AFTER_BUTTON = (By.CSS_SELECTOR, "#visibleAfter")

