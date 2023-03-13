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


class DroppablePageLocators:
    # simple
    SIMPLE_TAB = (By.CSS_SELECTOR, "#droppableExample-tab-simple")
    SIMPLE_DRAG_ME = (By.CSS_SELECTOR, "#draggable")
    SIMPLE_DROPPED = (By.CSS_SELECTOR, "#droppableExample-tabpane-simple #droppable")

    # accept
    ACCEPT_TAB = (By.CSS_SELECTOR, "#droppableExample-tab-accept")
    ACCEPT_ACCEPTABLE = (By.CSS_SELECTOR, "#acceptable")
    ACCEPT_NOT_ACCEPTABLE = (By.CSS_SELECTOR, "#notAcceptable")
    ACCEPT_DROPPABLE = (By.CSS_SELECTOR, "#acceptDropContainer #droppable")

    # prevent propogation
    PREVENT_TAB = (By.CSS_SELECTOR, "#droppableExample-tab-preventPropogation")
    PREVENT_DRAG_ME = (By.CSS_SELECTOR, "#dragBox")
    PREVENT_NOT_GREEDY_OUTER_BOX = (By.CSS_SELECTOR, "#notGreedyDropBox")
    PREVENT_NOT_GREEDY_INNER_BOX = (By.CSS_SELECTOR, "#notGreedyInnerDropBox")
    PREVENT_GREEDY_OUTER_BOX = (By.CSS_SELECTOR, "#greedyDropBox")
    PREVENT_GREEDY_INNER_BOX = (By.CSS_SELECTOR, "#greedyDropBoxInner")
    PREVENT_NOT_GREEDY_OUTER_BOX_TEXT = (By.CSS_SELECTOR, "#notGreedyDropBox > p")
    PREVENT_GREEDY_OUTER_BOX_TEXT = (By.CSS_SELECTOR, "#greedyDropBox > p")

    # revert draggable
    REVERT_TAB = (By.CSS_SELECTOR, "#droppableExample-tab-revertable")
    WILL_REVERT = (By.CSS_SELECTOR, "#revertable")
    NOT_REVERT = (By.CSS_SELECTOR, "#notRevertable")
    REVERT_DROP_HERE = (By.CSS_SELECTOR, "#revertableDropContainer #droppable")

