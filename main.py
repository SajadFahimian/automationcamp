from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# service = Service(ChromeDriverManager().install())
service = Service(executable_path="C:\chromedriver.exe")
options = Options()
options.add_experimental_option('detach', True)



driver = webdriver.Chrome(service=service, options=options)


driver.get("https://google.com")