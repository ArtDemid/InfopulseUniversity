from pages.objects.element_objects import InputTextElement
from pages.locators.internal_page_locators import InternalPageLocators as ipl
from pages.locators.sign_in_locators import SignInPageLocators as spl
from pages.locators.dashboard_page_locators import DashBoardLocators as dbl
from pages.objects.status_block import StatusBlock

from pages.base_page import Page
from selenium.webdriver.common.by import By

class SignInPage(Page):

    @property
    def username_field(self):
        return InputTextElement(
            self.find_visible_element(spl.USERNAME_FIELD))

    @property
    def password_field(self):
        return InputTextElement(
            self.find_visible_element(spl.PASSWORD_FIELD))

    @property
    def sign_in_button(self):
        return self.find_visible_element(spl.SIGN_IN_BUTTON)

    def fill_form(self, user):
        self.username_field.input(user.username)
        self.password_field.input(user.password)
        self.sign_in_button.click()
        self.find_visible_element(ipl.MAIL_LOCATOR)
        return DashboardPage(self.driver)

class InternalPage(Page):
        
    @property
    def sign_in_menu(self):
        return self.find_visible_element(
            ipl.SIGN_IN_MENU)

    def sign_in_click(self):
        self.sign_in_menu.click()
        return SignInPage(self.driver)

class MainPage(InternalPage):
    pass

class JoinPage(InternalPage):
    pass

class DashboardPage(Page):

    @property
    def status_input(self):
        return InputTextElement(
            self.find_visible_element(dbl.NEW_STATUS_FIELD))
    
    @property
    def send_button(self):
        return self.find_visible_element(dbl.SEND_BUTTON)

    @property
    def status_elements(self):
        return [StatusBlock(element) for element in self.driver.find_elements(*dbl.STATUS_BLOCK)]

    def create_status(self, text):
        self.status_input.input(text)
        self.send_button_click()

    def wait_new_status(self, elements):
        pass