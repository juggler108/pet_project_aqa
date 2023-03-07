from selenium.webdriver.common.by import By


class AccordianPageLocators:
    SECTION_ONE_HEADER = (By.CSS_SELECTOR, "#section1Heading")
    SECTION_ONE_TEXT = (By.CSS_SELECTOR, "#section1Content p")
    SECTION_TWO_HEADER = (By.CSS_SELECTOR, "#section2Heading")
    SECTION_TWO_TEXT = (By.CSS_SELECTOR, "#section2Content p")
    SECTION_THREE_HEADER = (By.CSS_SELECTOR, "#section3Heading")
    SECTION_THREE_TEXT = (By.CSS_SELECTOR, "#section3Content p")


