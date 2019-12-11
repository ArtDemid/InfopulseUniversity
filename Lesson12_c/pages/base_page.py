from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.expected_conditions import visibility_of_element_located, element_to_be_clickable
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

class Page:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)
        self.actions = ActionChains(driver)

    def is_element_present(self, locator):
        try:
            self.driver.find_element(*locator)
        except NoSuchElementException as ex:
            return False
        return True

    def find_visible_element(self, locator):
        element = self.wait.until(visibility_of_element_located(locator),
                                message=f"No visible element located {locator}") #this method expects tuple
        return element

    def find_clickable_element(self, locator):
        element = self.wait.until(element_to_be_clickable(locator),
                                message=f"No visible element located {locator}") #this method expects tuple
        return element