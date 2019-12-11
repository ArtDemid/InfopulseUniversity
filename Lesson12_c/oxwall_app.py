from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located, element_to_be_clickable
from custom_explicity_wait import presence_of_N_elements_located

class OxwallApp:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)
        self.actions = ActionChains(driver)

    def login_as(self, logged_user):
        driver = self.driver
        sign_in_menu = driver.find_element_by_class_name("ow_signin_label")
        sign_in_menu.click()
        username_field = driver.find_element_by_name("identity")
        username_field.clear()
        username_field.send_keys(logged_user.username)
        password_field = driver.find_element_by_name("password")
        password_field.clear()
        password_field.send_keys(logged_user.password)
        sign_in_button = driver.find_element_by_name("submit")
        sign_in_button.click()
        wait = WebDriverWait(driver, 5)
        wait.until(visibility_of_element_located((By.CLASS_NAME, "ow_mailbox_items_list")),
                   message=f"No visible element located {(By.CLASS_NAME, 'ow_mailbox_items_list')}")

    def logout_as(self, user):
        menu = self.driver.find_element(By.LINK_TEXT, user.full_name) #user
        self.actions.move_to_element(menu).perform()
        self.driver.find_element(By.XPATH, './/a[contains(@href,"sign-out")]').click()

    def create_status(self, text):
        driver = self.driver
        status_input = driver.find_element_by_name("status")
        status_input.send_keys(text)
        send_button = driver.find_element_by_name("save")
        send_button.click()

    def status_elements(self):
        return self.driver.find_elements_by_class_name("ow_newsfeed_content")

    def wait_new_status(self, elements):
        text_elements = self.wait.until(
            presence_of_N_elements_located(len(elements) + 1, (By.CLASS_NAME, "ow_newsfeed_content")),
            message=f"{(By.CLASS_NAME, 'ow_newsfeed_content')}")