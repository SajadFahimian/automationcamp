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
# options = Options()
# options.add_experimental_option('detach', True)
# options.add_argument("--incognito")
# options.add_argument("--headless")


# driver = webdriver.Chrome(service=service, options=options)

# actions = ActionChains(driver)


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



# element_1 = driver.find_element(By.ID, "drag1")
# element_2 = driver.find_element(By.ID, "div1")


# actions.move_to_element(element_1).click_and_hold().move_to_element(element_2).release().perform()

# actions.drag_and_drop(element_1, element_2).perform()

# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# driver.execute_script("scroll(0, 500)")

# driver.maximize_window()

# offset = driver.find_element(By.XPATH, "//*[text()='Lets you select only one option']").location

# print(offset)

# driver.find_element(By.ID, "option").click()

# actions.move_by_offset(offset['x'], offset['y']).click().perform()


# element_1 = driver.find_element(By.ID, "drag1")
# element_1_offset = element_1.location
# element_2_offset = driver.find_element(By.ID, "div1").location
# offset = {}
# offset['x'] = element_2_offset['x'] - element_1_offset['x']
# offset['y'] = element_2_offset['y'] - element_1_offset['y']
# actions.drag_and_drop_by_offset(element_1, offset['x'], offset['y']).perform()

# print(offset)

# sleep(2)

# sleep(10)
# current_path = Path(__file__).parent
# file_name = os.path.join(str(current_path), "screenshot.png")
# driver.save_screenshot(file_name)
# search_field = driver.find_element("name", "q")


#==============---- SESSION 10 ----==============
# driver.get("https://play2.automationcamp.ir/")
# driver.get("https://www.imdb.com/chart/top/")
# driver.implicitly_wait(0.1)
# driver.maximize_window()

# driver.execute_script("window.scrollTo(0, 500);")
# driver.execute_script("window.scrollTo(0, 500);")
# driver.execute_script("window.scrollBy(0, 500);")

# document_height = driver.execute_script("return document.body.scrollHeight;")
# document_width = driver.execute_script("return document.body.scrollWidth;")

# print(document_height)
# print(document_width)

# element = driver.find_element(By.XPATH, "//h3[text()='235. The Handmaiden']/parent::a")
# driver.execute_script("arguments[0].scrollIntoView()", element)


# def scroll_find_to_element(movie_name, scroll_pixel):
#     for i in range(10):
#         try:
#             driver.find_element(By.XPATH, f"//h3[contains(text(), '{str(movie_name)}')]/parent::*")
#             print(f"Found the {str(movie_name)}")
#             return
#         except:
#             driver.execute_script(f"window.scrollBy(0, {str(scroll_pixel)});")
#             sleep(0.5)
#     raise Exception(f"Not found the {str(movie_name)}")


# scroll_find_to_element("235", 3100)

# driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")
# driver.execute_script("window.scrollBy(0, 0);")
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# driver.set_window_size(400, 600)

# element = driver.find_element(By.XPATH, "//td[text()='Personal Shopper']")
# driver.execute_script("arguments[0].scrollIntoView();", element)


# element = driver.find_element(By.XPATH, "//h3[contains(text(), 'The Iron Giant')]/parent::a")
# print(element)
# print(element.is_displayed())


# el1 = driver.find_element(By.ID, "option")
# el2 = driver.find_element(By.NAME, "message")

# actions.move_to_element(el1).click_and_hold().move_to_element(el2).release().perform()

# page_element = driver.find_element(By.TAG_NAME, "html")

# page_element.send_keys(Keys.END)
# sleep(2)
# page_element.send_keys(Keys.HOME)

# def scroll_find_to_element(movie_name):
#     page_element = driver.find_element(By.XPATH, "//html[@class=' scriptsOn']")

#     for i in range(10):
#         try:
#             driver.find_element(By.XPATH, f"//h3[contains(text(), '{str(movie_name)}')]/parent::*")
#             print(f"Found the {str(movie_name)}")
#             return
#         except:
#             actions.send_keys_to_element(page_element, Keys.PAGE_DOWN).perform()
#             # actions.send_keys_to_element(page_element, Keys.DOWN).perform()
#             # actions.send_keys_to_element(page_element, Keys.DOWN).perform()
#             sleep(0.5)
#     raise Exception(f"Not found the {str(movie_name)}")



# scroll_find_to_element("lkdfjhll")

# element = driver.find_element(By.XPATH, "//h3[contains(text(), 'The Hand')]/parent::a")

# element.location_once_scrolled_into_view

# driver.set_window_size(200, 800)

# element = driver.find_element(By.XPATH, "//td[text()='Personal Shopper']")
# page_element = driver.find_element(By.TAG_NAME, "html")
# actions.send_keys_to_element(page_element, Keys.END).perform()
# sleep(1)
# element.location_once_scrolled_into_view


#==============---- SESSION 11 ----==============
# driver.get("https://play2.automationcamp.ir/")
# driver.get("https://material.angular.io/components/categories")
# driver.get("https://material.angular.io/components/slide-toggle/examples")
# driver.get("https://material.angular.io/components/input/examples#input-error-state-matcher")
# driver.implicitly_wait(2)

# driver.find_element(By.XPATH, "//span[contains(text(), 'Got it')]").click()

# element = driver.find_element(By.TAG_NAME, "h1")
# text = element.text
# print(text)

# element = driver.find_element(By.XPATH, "(//span[@class='mdc-button__label' and text()='Components']//..)[1]")
# element.click()
# attr_1 = element.get_attribute("class")
# assert "selected" in attr_1, "Element is not selected"
# print("attr 1: " + attr_1)

# driver.find_element(By.XPATH, "(//span[@class='mdc-button__label' and text()='CDK']//..)[1]").click()
# attr_2 = element.get_attribute("class")
# assert "selected" not in attr_2, "Element is selected"
# print("attr 2: " + attr_2)

# rbt_accent = driver.find_element(By.ID, "mat-radio-3")
# assert "checked" in rbt_accent.get_attribute("class")

# element = driver.find_element(By.ID, "mat-radio-2")
# attr_1 = element.get_attribute("class")
# assert "checked" not in attr_1
# print("attr 1: " + attr_1)

# element.click()
# attr_2 = element.get_attribute("class")
# assert "checked" in attr_2
# print("attr 2: " + attr_2)

# assert "checked" not in rbt_accent.get_attribute("class")

# toggle = driver.find_element(By.ID, "mat-mdc-slide-toggle-1-button")
# assert "checked" not in toggle.get_attribute("class")
# toggle.click()
# assert "checked" in toggle.get_attribute("class")

# assert "disabled" not in toggle.get_attribute("class")

# checkbox = driver.find_element(By.ID, "mat-mdc-checkbox-2")
# assert "checked" not in checkbox.get_attribute("class")
# checkbox.click()
# assert "checked" in checkbox.get_attribute("class")

# assert "disabled" in toggle.get_attribute("class")

# input_element = driver.find_element(By.ID, "mat-input-1")
# text = "This is session 11"
# input_element.send_keys(text)
# input_value = input_element.get_attribute("value")
# assert text == input_value

# parent_el = driver.find_element(By.XPATH, "//*[@id='mat-input-1']/ancestor::mat-form-field")
# assert 'dirty' not in parent_el.get_attribute("class")
# input_el = driver.find_element(By.ID, "mat-input-1")
# input_el.send_keys("Hello new world")
# assert 'dirty' in parent_el.get_attribute("class")

#==============---- SESSION 12 ----==============
from datetime import datetime
# driver.get("https://play1.automationcamp.ir/expected_conditions.html")
# driver.implicitly_wait(1)

# print(datetime.now())
# sleep(3)
# print(datetime.now())

# driver.implicitly_wait(4)
# print(datetime.now())
# try:
#     driver.find_element(value="kdjf;ljd;j")
# except:
#     print(datetime.now())

def wait_until_element_has_an_attribute(element_selector, element_locator, attribute, attribute_value, timeout=5, exact=True):
    for i in range(timeout * 10):
        try:
            element = driver.find_element(element_selector, element_locator)
            if exact:
                assert attribute_value == element.get_attribute(attribute)
            else:
                assert attribute_value in element.get_attribute(attribute)
            return
        except:
            sleep(0.1)
    raise Exception(f"Element attribute \"{attribute}\" not in or not equale \"{attribute_value}\"")

def wait_until_element_has_not_an_attribute(element_selector, element_locator, attribute, attribute_value, timeout=5, exact=True):
    for i in range(timeout * 10):
        try:
            element = driver.find_element(element_selector, element_locator)
            if exact:
                assert attribute_value != element.get_attribute(attribute)
            else:
                assert attribute_value not in element.get_attribute(attribute)
            return
        except:
            sleep(0.1)
    raise Exception(f"Element attribute \"{attribute}\" in or equale \"{attribute_value}\"")

# trigger = driver.find_element(By.ID, "enabled_trigger")
# trigger.location_once_scrolled_into_view

# wait_until_element_has_an_attribute(By.ID, "enabled_target", "class", "danger", exact=False)
# wait_until_element_has_not_an_attribute(By.ID, "enabled_target", "class", "success", exact=False)
# trigger.click()
# wait_until_element_has_not_an_attribute(By.ID, "enabled_target", "class", "danger", exact=False)
# wait_until_element_has_an_attribute(By.ID, "enabled_target", "class", "success", exact=False)

def wait_until_element_is_enabled(selector, locator, timeout=5):
    for i in range(timeout * 10):
        try:
            element = driver.find_element(selector, locator)
            assert element.is_enabled()
            
            return
        except:
            sleep(0.1)
    raise Exception("The element is disabled")
    
def wait_until_element_is_not_enabled(selector, locator, timeout=5):
    for i in range(timeout * 10):
        try:
            element = driver.find_element(selector, locator)
            assert not element.is_enabled()
            
            return
        except:
            sleep(0.1)
    raise Exception("The element is ensabled")

# trigger = driver.find_element(By.ID, "enabled_trigger")
# trigger.location_once_scrolled_into_view

# wait_until_element_is_not_enabled(By.ID, "enabled_target")
# trigger.click()
# wait_until_element_is_enabled(By.ID, "enabled_target", 4)


def wait_until_element_is_visible(selector, locator, timeout=5):
    for i in range(timeout * 10):
        try:
            element = driver.find_element(selector, locator)
            assert element.is_displayed()
            
            return
        except:
            sleep(0.1)
    raise Exception("The element is not visible")
    
def wait_until_element_is_not_visible(selector, locator, timeout=5):
    for i in range(timeout * 10):
        try:
            element = driver.find_element(selector, locator)
            assert not element.is_displayed()
            
            return
        except:
            sleep(0.1)
    raise Exception("The element is visible")



# trigger = driver.find_element(By.ID, "visibility_trigger")
# trigger.location_once_scrolled_into_view
# wait_until_element_is_not_visible(By.ID, "visibility_target")
# trigger.click()
# wait_until_element_is_visible(By.ID, "visibility_target")

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# trigger = driver.find_element(By.ID, "enabled_trigger")
# trigger.location_once_scrolled_into_view
# wait = WebDriverWait(driver, 5)
# trigger.click()
# element = wait.until(EC.element_to_be_clickable((By.ID, "enabled_target")))
# print(element)
# if element:
#     element.click()

def wait_until_page_is_loaded(timeout=5):
    for i in range(timeout * 2):
        try:
            state = driver.execute_script("return document.readyState")
            assert state == "complete"
            return
        except:
            sleep(0.5)
    raise Exception(f"Page not loaded in {str(timeout)} second")

# driver.get("https://archive.org/details/audio_bookspoetry")
# wait_until_page_is_loaded(1)


#==============---- SESSION 13 ----==============
# driver.get("https://the-internet.herokuapp.com/javascript_alerts")
# driver.get("https://material.angular.io/components/dialog/examples")
# driver.get("https://material.angular.io/components/snack-bar/examples")
# driver.get("https://material.angular.io/components/tooltip/examples#tooltip-message")

# driver.implicitly_wait(1)

# driver.find_element(By.XPATH, "//span[contains(text(), 'Got it')]").click()

from selenium.webdriver.common.alert import Alert
# alert = Alert(driver)

# result = driver.find_element(By.ID, "result")

# driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()
# assert alert.text == "I am a JS Alert"
# alert.accept()
# assert result.text == "You successfully clicked an alert"

# driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()
# assert alert.text == "I am a JS Confirm"
# sleep(1)
# alert.accept()
# assert result.text == "You clicked: Ok"

# driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()
# assert alert.text == "I am a JS Confirm"
# sleep(1)
# alert.dismiss()
# assert result.text == "You clicked: Cancel"

# text = "Sajad try to programer"
# driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']").click()
# assert alert.text == "I am a JS prompt"
# sleep(1)
# alert.send_keys(text)
# sleep(1)
# alert.accept()
# assert text in result.text
# assert text in driver.page_source

# driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']").click()
# assert alert.text == "I am a JS prompt"
# sleep(1)
# alert.dismiss()
# assert 'null' in result.text
# assert 'null' in driver.page_source

# offset = driver.find_element(By.XPATH, "(//*[@class='mdc-button__label' and text()='CDK'])[1]").location

# driver.find_element(By.XPATH, "(//span[text()='Open dialog']/..)[1]").click()
# driver.find_element(By.XPATH, "//h3[text()='Develop across all platforms']")
# driver.find_element(By.XPATH, "//button//span[text()='Cancel']")
# driver.find_element(By.XPATH, "//button//span[text()='Install']")

# actions.move_by_offset(offset['x'], offset['y']).pause(0.5).click().perform()

# driver.find_element(By.XPATH, "(//span[text()='Open dialog']/..)[1]").click()

# timeout_input = driver.find_element(By.ID, "mat-input-1")
# timeout_input.clear()
# timeout_input.send_keys(1)
# driver.find_element(By.XPATH, "(//span[@class='mdc-button__label' and normalize-space(text())='Pizza party']/ancestor::button)[2]").click()



# driver.find_element(By.XPATH, "//*[@class='cdk-overlay-container']//*[contains(text(), 'Pizza party!!!')]")


# driver.find_element(By.XPATH, "//*[@class='cdk-overlay-container']//*[contains(text(), 'Pizza party!!!')]")


# driver.find_element(By.TAG_NAME, "snack-bar-component-example-snack")
# driver.find_element(By.XPATH, "//snack-bar-component-example-snack")
# driver.find_element(By.XPATH, "//snack-bar-component-example-snack//*[contains(text(), 'Pizza party!!!')]")

def check_tooltip_is_visible(elements: list, text: str, exact=True) -> None:
    for el in elements:
        try:
            if exact:
                assert el.text == text
            else:
                assert text in el.text
            return
        except:
            pass
    raise Exception("Can not find any tooltip with message: " + text)
    


# input_element = driver.find_element(By.ID, "mat-input-2")
# text = "Automation Camp"
# input_element.clear()
# input_element.send_keys(text)
# action_button = driver.find_element(By.XPATH, "(//span[@class='mdc-button__label' and contains(text(), 'Action')]/parent::button)[6]")
# actions.move_to_element(action_button).perform()
# elements = driver.find_elements(By.XPATH, "//*[@class='cdk-overlay-container']/descendant::*")
# assert len(elements) > 0
# check_tooltip_is_visible(elements, text)
# actions.move_to_element(input_element).perform()
# elements = driver.find_elements(By.XPATH, "//*[@class='cdk-overlay-container']/descendant::*")
# assert len(elements) == 0



#==============---- SESSION 14 ----==============

# current_path = Path(__file__).parent.parent
# user_dir = os.path.join(current_path, 'user_dir')

# path = "C:/Users/Home/Desktop/Project/automationcamp/user_data"
# options = webdriver.ChromeOptions()
# options.add_argument("user-data-dir=" + str(user_dir))
# options.add_experimental_option("detach", True)

# driver = webdriver.Chrome(service=service, options=options)
# wait = WebDriverWait(driver, 10)
# actions = ActionChains(driver)

# driver.get("https://quera.org/accounts/signup")
# driver.get("https://quera.org")
# driver.get("https://web.bale.ai/chat")
# driver.maximize_window()
# driver.implicitly_wait(3)

# windows = driver.window_handles
# driver.switch_to.window(windows[0])

# input_email = driver.find_element(By.XPATH, "//input[@type='email']")
# input_password = driver.find_element(By.XPATH, "//input[@type='password']")
# submit_button = driver.find_element(By.ID, "signup-button")

# email = "automationcamp@info.com"
# password = "0915automationir"

# recaptcha = wati.until(EC.presence_of_element_located((By.XPATH, "//*[@class='recaptcha-checkbox-border']")))
# recaptcha = driver.find_element(By.XPATH, "//*[@class='recaptcha-checkbox-border']")


# input_email.send_keys(email)
# input_password.send_keys(password)
# actions.move_to_element(recaptcha).click().perform()

# driver.get("https://patrickhlauke.github.io/recaptcha/")

# driver.switch_to.frame(wait.until(EC.presence_of_element_located((By.XPATH, "//iframe[@role='presentation']"))))
# driver.find_element(By.XPATH, "//div[@class='recaptcha-checkbox-border']").click()

# driver.switch_to.window(windows[0])
# submit_button = wait.until(EC.element_to_be_clickable((By.ID, "signup-button")))
# submit_button.click()

# driver.find_element(By.XPATH, "//button[text()='متوجه شدم']").click()
# mobile_number = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='شماره همراه']")))
# mobile_number.send_keys("09306813527")

# submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='submit-button']")))
# submit_button.click()

# input_number = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='کد ورود']")))
# number = input("please enter your number: ")
# input_number.send_keys(number)

# submit_button_1 = wait.until(EC.element_to_be_clickable(()))


#==============---- SESSION 15 ----==============

# driver.get("https://csreis.github.io/tests/cross-site-iframe.html")
# driver.get("https://play1.automationcamp.ir/frames.html")

# condition = wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, "frame1")))
# condition = wait.until(EC.frame_to_be_available_and_switch_to_it("frame1"))

# if condition:

#     text = driver.find_element(By.TAG_NAME, "body").text

#     assert text == "Initial page"

# driver.switch_to.default_content()
# driver.find_element(By.XPATH, "//h1")

# driver.switch_to.frame("frame1")
# driver.find_element(By.ID, "click_me_1").click()
# sleep(1)

# driver.switch_to.frame("frame2")
# driver.find_element(By.ID, "click_me_2").click()
# sleep(1)

# driver.switch_to.parent_frame()
# driver.switch_to.frame("frame3")
# driver.switch_to.frame("frame4")
# driver.find_element(By.ID, "click_me_4").click()
# sleep(1)

def get_frame_of_element(selector, locator, _driver):
    all_frames = _driver.find_elements(By.TAG_NAME, "iframe")

    for fra in all_frames:
        _driver.switch_to.frame(fra)
        try:
            el = _driver.find_element(selector, locator)
            driver.switch_to.default_content()
            return fra
        except:
            pass
    
    raise Exception("Could not find the element in all frames")


#==============---- SESSION 16 ----==============
# driver.get("https://play2.automationcamp.ir/")

# driver.find_element(By.CSS_SELECTOR, "input[id='fname']").send_keys('outomationcamp')
# driver.find_element(By.CSS_SELECTOR, "input#fname").send_keys('outomationcamp')


#==============---- SESSION 17 ----==============
options = webdriver.ChromeOptions()

prefs = {
    # "profile.default_content_setting_values.geolocation": 2,
    # "profile.default_content_setting_values.media_stream_camera": 1,
    # "profile.default_content_setting_values.media_stream_mic": 1,
    "profile.default_content_setting_values.notifications": 2,
}

# 0 > ask, 1 > allow, 2 > deny
options.add_experimental_option("prefs", prefs)
options.add_argument("start-maximized")

driver = webdriver.Chrome(service=service, options=options)
# driver.get("https://whatmylocation.com/")
driver.get("https://play2.automationcamp.ir/")
driver.execute_script("Notification.requestPermission()")
sleep(10)










sleep(5)

driver.quit()