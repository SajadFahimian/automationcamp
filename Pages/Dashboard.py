from Locators import admin_dashboard

class Dashboard:
    def __init__(self, driver):
        self.driver = driver

        



    def check_dashboard(self):

        self.driver.find_element(admin_dashboard['by'], admin_dashboard['value'])