from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located, element_to_be_clickable
from selenium.common.exceptions import NoSuchElementException


class Page:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)
        self.actions = ActionChains(driver)

    def is_element_present(self, locator):
        try:
            self.driver.find_element(*locator)
        except NoSuchElementException:
            return False
        return True

    def find_visible_element(self, locator):
        el = self.wait.until(visibility_of_element_located(locator),
                             message=f"No visible element located {locator}")
        return el

    def find_clickable_element(self, locator):
        el = self.wait.until(element_to_be_clickable(locator),
                             message=f"No clickable element located {locator}")
        return el