from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from webdriver_manager.chrome import ChromeDriverManager

from time import sleep
import os
from pathlib import Path

# service = Service(ChromeDriverManager().install())
service = Service(executable_path="C:\chromedriver.exe")
options = Options()
options.add_experimental_option('detach', True)
# options.add_argument("--incognito")
# options.add_argument("--headless")


driver = webdriver.Chrome(service=service, options=options)

actions = ActionChains(driver)


# driver.get("https://google.com")

# window_title = driver.title

# print(window_title)

# sleep(2)



# driver.back()

# sleep(2)

# driver.forward()
# sleep(3)
# driver.refresh()

# driver.switch_to.new_window('tab')

# sleep(2)

# driver.switch_to.new_window('window')
# driver.get("https://aparat.com")

# sleep(2)

# yahoo_window = driver.current_window_handle

# all_handle = driver.window_handles

# driver.switch_to.window(all_handle[0])
# sleep(3)
# driver.switch_to.window(all_handle[1])
# driver.get("https://yahoo.com")

# driver.close()

# search_field = driver.find_element("name", "q")
# search_field.send_keys("wikipedia")
# search_field.send_keys(Keys.RETURN)


# window_size = driver.get_window_size()

# print(window_size)

# driver.set_window_size(800, 600)


# window_position = driver.get_window_position()

# print(window_position)

# driver.set_window_position(400, 500)

# sleep(1)

# driver.minimize_window()


# sleep(2)
# driver.maximize_window()


# sleep(2)
# driver.fullscreen_window()

# driver.execute_script("console.log(\"hello world\")")

# sleep(2)
# driver.get("https://yahoo.com")
# driver.get("https://wikipedia.com")

# el1 = driver.find_element(By.ID, "searchInput")
# el1 = driver.find_element(By.CSS_SELECTOR, "#searchInput")
# el1.send_keys("Hello world")


# el2 = driver.find_element(By.XPATH, "//input[@type='search']")

# assert el1 == el2

# el3 = driver.find_element(By.XPATH, "//*[text()='فارسی']")
# el3.click()

# el4 = driver.find_element(By.TAG_NAME, 'select')
# el4.click()

# driver.find_element(By.LINK_TEXT, "Download Wikipedia for Android or iOS").click()

# driver.find_element(By.PARTIAL_LINK_TEXT, "Download").click()

# driver.find_element(By.CLASS_NAME, "svg-search-icon").click()

# driver.find_element(By.CSS_SELECTOR, ".svg-search-icon").click()




# driver.get("https://google.com")

# search_element = driver.find_element(By.NAME, 'q')
# search_element.send_keys("selenium" + Keys.ENTER)
# actions.key_down(Keys.CONTROL).send_keys('a').perform()


# actions.key_down(Keys.SHIFT).send_keys_to_element(search_element, 'selenium').perform()
# actions.key_down(Keys.SHIFT).send_keys_to_element(search_element, 'selenium').key_up(Keys.SHIFT).send_keys(" selenium").perform()


# search_element.clear()
# search_element.click()

# actions.key_down(Keys.CONTROL).send_keys('a').send_keys(Keys.DELETE).perform()


# driver.get("https://play2.automationcamp.ir/")

# double_click = driver.find_element(By.XPATH, "//button[text()='Double-click me']")

# actions.double_click(double_click).perform()

# result = driver.find_element(By.XPATH, "(//p[@id='demo' ])[1]").text

# assert result == "Your Sample Double Click worked!"


# el = driver.find_element(By.XPATH, "//*[@id='fname']")
# actions.context_click(el).perform()

# el = driver.find_element(By.XPATH, "//*[@class='tooltip']")
# actions.move_to_element(el).perform()

# driver.get("https://demos.telerik.com/kendo-ui/circular-gauge/index")
# driver.find_element(By.ID, "onetrust-accept-btn-handler").click()
# driver.execute_script("scroll(0, 400)")



# element_1 = driver.find_element(By.XPATH, "//*[contains(@class, 'k-button-increase')]")
# element_2 = driver.find_element(By.XPATH, "//*[contains(@class, 'k-button-decrease')]")

# actions.click_and_hold(element).perform()
# actions.click_and_hold(element_1).pause(3).release().click_and_hold(element_2).pause(3).release().perform()


driver.get("https://play2.automationcamp.ir/")

# element_1 = driver.find_element(By.ID, "drag1")
# element_2 = driver.find_element(By.ID, "div1")


# actions.move_to_element(element_1).click_and_hold().move_to_element(element_2).release().perform()

# actions.drag_and_drop(element_1, element_2).perform()

# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

driver.execute_script("scroll(0, 500)")

# driver.maximize_window()

# offset = driver.find_element(By.XPATH, "//*[text()='Lets you select only one option']").location

# print(offset)

# driver.find_element(By.ID, "option").click()

# actions.move_by_offset(offset['x'], offset['y']).click().perform()


element_1 = driver.find_element(By.ID, "drag1")
element_1_offset = element_1.location
element_2_offset = driver.find_element(By.ID, "div1").location
offset = {}
offset['x'] = element_2_offset['x'] - element_1_offset['x']
offset['y'] = element_2_offset['y'] - element_1_offset['y']
actions.drag_and_drop_by_offset(element_1, offset['x'], offset['y']).perform()

print(offset)

sleep(2)

# sleep(10)
# current_path = Path(__file__).parent
# file_name = os.path.join(str(current_path), "screenshot.png")
# driver.save_screenshot(file_name)
# search_field = driver.find_element("name", "q")

sleep(5)

driver.quit()