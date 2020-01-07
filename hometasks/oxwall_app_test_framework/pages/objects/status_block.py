from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from pages.locators.dashboard_page_locators import StatusBlockLocators as stbl

from value_models.user_model import User


class StatusBlock:

    def __init__(self, webelement):
        self.webelement = webelement
    
    @property
    def text(self):
        return self.webelement.find_element(*stbl.STATUS_TEXT).text

    @property
    def user(self):
        user_element = self.webelement.find_element(*stbl.STATUS_TEXT)
        return User(
            username = user_element.get_attribute("href").split("/")[-1],
            full_name =user_element.text
        )
    
    @property
    def time(self):
        return self.webelement.find_element(*stbl.STATUS_TIME).text
