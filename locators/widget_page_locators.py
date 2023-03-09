from selenium.webdriver.common.by import By


class AccordianPageLocators:
    SECTION_ONE_HEADER = (By.CSS_SELECTOR, "#section1Heading")
    SECTION_ONE_TEXT = (By.CSS_SELECTOR, "#section1Content p")
    SECTION_TWO_HEADER = (By.CSS_SELECTOR, "#section2Heading")
    SECTION_TWO_TEXT = (By.CSS_SELECTOR, "#section2Content p")
    SECTION_THREE_HEADER = (By.CSS_SELECTOR, "#section3Heading")
    SECTION_THREE_TEXT = (By.CSS_SELECTOR, "#section3Content p")


class AutoCompletePageLocators:
    MULTIPLE_AUTO_COMPLETE_INPUT = (By.CSS_SELECTOR, "#autoCompleteMultipleInput")
    MULTIPLE_VALUE = (By.CSS_SELECTOR, ".auto-complete__multi-value")
    MULTIPLE_REMOVE_BUTTON = (By.CSS_SELECTOR, ".auto-complete__multi-value svg path")
    MULTIPLE_REMOVE_ALL_BUTTON = (By.CSS_SELECTOR, ".auto-complete__clear-indicator svg path")
    SINGLE_AUTO_COMPLETE_INPUT = (By.CSS_SELECTOR, "#autoCompleteSingleInput")
    SINGLE_VALUE = (By.CSS_SELECTOR, ".auto-complete__single-value")


class DatePickerPageLocators:
    DATE_INPUT = (By.CSS_SELECTOR, "#datePickerMonthYearInput")
    DATE_SELECT_YEAR = (By.CSS_SELECTOR, ".react-datepicker__year-select")
    DATE_SELECT_MONTH = (By.CSS_SELECTOR, ".react-datepicker__month-select")
    DATE_SELECT_DAY_LIST = (By.CSS_SELECTOR, ".react-datepicker__day")

    DATE_AND_TIME_INPUT = (By.CSS_SELECTOR, "#dateAndTimePickerInput")
    DATE_AND_TIME_YEAR = (By.CSS_SELECTOR, ".react-datepicker__year-read-view--selected-year")
    DATE_AND_TIME_MONTH = (By.CSS_SELECTOR, ".react-datepicker__month-read-view--selected-month")
    DATE_AND_TIME_TIME_LIST = (By.CSS_SELECTOR, ".react-datepicker__time-list-item")
    DATE_AND_TIME_YEAR_LIST = (By.CSS_SELECTOR, ".react-datepicker__year-option")
    DATE_AND_TIME_MONTH_LIST = (By.CSS_SELECTOR, ".react-datepicker__month-option")

