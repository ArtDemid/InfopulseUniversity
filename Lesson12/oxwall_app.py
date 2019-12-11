from selenium.webdriver.support.expected_conditions import visibility_of_element_located

class OxwallApp:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)
        self.actions = ActionsChains(driver)

    def login_as(self, driver, username, password):
        sign_in_menu = driver.find_element_by_class_name("ow_sign_login")
        sign_in_menu.click()

        user_name_field = driver.find_element_by_name("identity")
        user_name_field.clear()  
        user_name_field.send_keys(username)

        password_field = driver.find_element_by_name("password")
        password_field.clear()
        password_field.send_keys(password)

        sign_in_button = driver.find_element_by_name("submit")
        sign_in_button.click()
        wait = WebDriverWait(driver, 5)
        wait.until(visibility_of_element_located((By.CLASS_NAME, "base_dashboard")), 
                message=f"NO visible element located {(By.CLASS_NAME, 'base_dashboard')}")

    def log_out(self, user):
        menu = driver.find_element(By.LINK_TEXT, 'Admin')
        actions = ActionChains(driver)
        actions.move_to_element(menu).perform()
        driver.find_element(By.XPATH, './/a[contains(@href,"sign-out")]').click()