from selenium.webdriver.common.by import By

class InternalPageLocators:
    USER_MENU = (By.CSS_SELECTOR, ".ow_console_items_wrap div:nth-child(5)")
    SIGN_IN_MENU = (By.CLASS_NAME, "ow_signin_label")
    ACTIVE_MENU = (By.CSS_SELECTOR, ".ow_responsive_menu .ow_main_menu .active")
    MAIL_LOCATOR  = (By.CLASS_NAME, "ow_mailbox_items_list")
    MAIN_MENU = ()
    DASHBOARD_MENU = ()