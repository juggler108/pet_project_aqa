from selenium.webdriver.common.by import By


class SortablePageLocators:
    TAB_LIST = (By.CSS_SELECTOR, "#demo-tab-list")
    VERTICAL_ITEM_LIST = (By.CSS_SELECTOR, ".vertical-list-container .list-group-item")

    TAB_GRID = (By.CSS_SELECTOR, "#demo-tab-grid")
    GRID_ITEM_LIST = (By.CSS_SELECTOR, ".create-grid .list-group-item")


class SelectablePageLocators:
    TAB_LIST = (By.CSS_SELECTOR, "#demo-tab-list")
    VERTICAL_ITEM_LIST = (By.CSS_SELECTOR, "#verticalListContainer .list-group-item")
    VERTICAL_LIST_ITEM__ACTIVE = (By.CSS_SELECTOR, "#verticalListContainer .list-group-item.active")

    TAB_GRID = (By.CSS_SELECTOR, "#demo-tab-grid")
    GRID_ITEM_LIST = (By.CSS_SELECTOR, "#gridContainer .list-group-item")
    GRID_ITEM_ACTIVE = (By.CSS_SELECTOR, "#gridContainer .list-group-item.active")


class ResizablePageLocators:
    RESIZABLE_BOX = (By.CSS_SELECTOR, "#resizableBoxWithRestriction")
    RESIZABLE_BOX_HANDLE = (By.CSS_SELECTOR, "#resizableBoxWithRestriction .react-resizable-handle")
    RESIZABLE = (By.CSS_SELECTOR, "#resizable")
    RESIZABLE_HANDLE = (By.CSS_SELECTOR, "#resizable .react-resizable-handle")
