from Locators import username_input, password_input, login_button

class Login:
    def __init__(self, driver):
        self.driver = driver


    def enter_username(self, username):
        self.driver.find_element(username_input['by'], username_input['value']).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(password_input['by'], password_input['value']).send_keys(password)

    def click_on_login_button(self):
        self.driver.find_element(login_button['by'], login_button['value']).click()
