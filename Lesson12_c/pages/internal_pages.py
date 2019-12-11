from pages.base_page import Page
from selenium.webdriver.common.by import By
from pages.locators import *

class SignInPage(Page):
    def __init__(self, driver):
        super.__init__(driver) #Call init of base class
        self.username_field = self.find_visible_element(SignInPageLocators.USERNAME_FIELD)
        self.password_field = self.find_visible_element(SignInPageLocators.PASSWORD_FIELD)
        self.sign_button = self.find_visible_element(SignInPageLocators.SIGN_IN_BUTTON)

    def fill_form(self, user):
        self.username_field.clear()
        self.username_field.send_keys(user.username)
        self.password_field.clear()
        self.password_field.send_keys(user.password)
        self.find_visible_element((By.CLASS_NAME, "ow_mailbox_items_list"))
        return DashboardPage(self.driver)


'''class InternalPage(Page):

    def __init__(self, driver):
        super.__init__(driver) #Call init of base class
        self.sign_in_menu = self.find_visible_element((By.CLASS_NAME, ""))
        #self.sign_in_menu = self.driver.find
    
    def sign_in_click(self):
        self.sign_in_menu.click()
        return SignInPage(self.driver)

    def login_as(self, logged_user):
        pass'''

class InternalPage(Page):

    @property
    def username_field(self):
        return self.find_visible_element((By.NAME, "identity"))

    @property
    def password_field(self):
        return self.find_visible_element((By.NAME, "password"))   
    @property
    def sign_in_button(self):
        return self.find_visible_element((By.NAME, "submit"))


class MainPage(InternalPage):
    pass

class JoinPage(InternalPage):
    pass

class DashboardPage():
    pass