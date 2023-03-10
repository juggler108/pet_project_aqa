from selenium.webdriver.common.by import By


class SortablePageLocators:
    TAB_LIST = (By.CSS_SELECTOR, "#demo-tab-list")
    VERTICAL_ITEM_LIST = (By.CSS_SELECTOR, ".vertical-list-container .list-group-item")

    TAB_GRID = (By.CSS_SELECTOR, "#demo-tab-grid")
    GRID_ITEM_LIST = (By.CSS_SELECTOR, ".create-grid .list-group-item")
