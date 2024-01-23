# import os
import sys

# parent_dir = os.path.dirname(os.path.realpath(__file__))

sys.path.append("../automationcamp")



from Pages.Login import Login
from Pages.Dashboard import Dashboard




from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from time import sleep

import unittest

class Test_Login(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        


        service = Service(executable_path='C:\chromedriver.exe')
        options = Options()

        options.add_experimental_option('detach', True)



        cls.driver = webdriver.Chrome(service=service)
        cls.driver.implicitly_wait(20)



    def test_valid_login(self):
        self.driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
        login = Login(self.driver)
        dashboard = Dashboard(self.driver)



        login.enter_username('Admin')
        login.enter_password('admin123')
        login.click_on_login_button()
        dashboard.check_dashboard()


        sleep(10)


    def test_invalid_login(self):
        self.driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
        login = Login(self.driver)
        dashboard = Dashboard(self.driver)



        login.enter_username('Admin')
        login.enter_password('admin1234')
        login.click_on_login_button()
        dashboard.check_dashboard()


        sleep(10)


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()




if __name__ == "__main__":
    unittest.main()