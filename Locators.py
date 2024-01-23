from selenium.webdriver.common.by import By



username_input = {"by": By.NAME, "value": "username"}
password_input = {"by": By.NAME, "value": "password"}
login_button = {"by": By.TAG_NAME, "value": "button"}

admin_dashboard = {"by": By.XPATH, "value": "//span[text()='Admin']"}

