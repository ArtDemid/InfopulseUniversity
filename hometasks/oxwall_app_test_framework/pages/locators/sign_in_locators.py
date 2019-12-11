from selenium.webdriver.common.by import By

class SignInPageLocators:
    USERNAME_FIELD = (By.NAME, "identity")
    PASSWORD_FIELD = (By.NAME, "password")
    SIGN_IN_BUTTON = (By.NAME, "submit")