from selenium.webdriver.common.by import By

class DashBoardLocators:
    STATUS_BLOCK = (By.XPATH, "//li[contains(@id, 'action-feed')]")
    STATUS_TEXT = (By.CLASS_NAME, "w_newsfeed_content")
    STATUS_USER = (By.CSS_SELECTOR, ".ow_newsfeed_string > a")
    STATUS_TIME  = (By.CLASS_NAME, "a.create_time.ow_newsfeed_date")
    NEW_STATUS_FIELD = ()
    SEND_BUTTON = ()

class StatusBlockLocators:
    STATUS_TEXT = (By.CLASS_NAME, 'ow_newsfeed_content')
    STATUS_USER = (By.CSS_SELECTOR, ".ow_newsfeed_string > a")
    STATUS_TIME = (By.CSS_SELECTOR, "a.create_time.ow_newsfeed_date")