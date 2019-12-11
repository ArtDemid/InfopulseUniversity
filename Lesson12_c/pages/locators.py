from selenium.webdriver.common.by import By

class SignInPageLocators:

    USERNAME_FIELD = (By.NAME, "identity")
    PASSWORD_FIELD = (By.NAME, "password")
    SIGN_IN_BUTTON = (By.NAME, "submit")

class InternalPageLocators:
    USER_MENU = (By.CSS_SELECTOR, "")
    SIGN_IN_MENU = (By.CLASS_NAME, "")
    ACTIVE_MENU = (By.CSS_SELECTOR, "")
    MAIN_MENU = ()
    DASHBOARD_MENU = ()

class MainPageLocators:
    pass


