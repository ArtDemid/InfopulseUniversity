from  pages.internal_pages import MainPage, DashboardPage, SignInPage

class OxwallManager:

    def __init__(self, driver):
        self.driver = driver
        self.main_page = MainPage(driver)
        self.dashboard_page = DashboardPage(driver)
        self.sign_in_page = SignInPage(driver)