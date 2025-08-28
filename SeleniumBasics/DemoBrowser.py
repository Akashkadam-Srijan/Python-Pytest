import time

from selenium import webdriver
from selenium.webdriver.common.by import By

### Invoke Browser
driver = webdriver.Chrome()
#driver = webdriver.Firefox()
#driver = webdriver.Safari()
driver.get("https://www.nasdaq.com/")
driver.maximize_window()
driver.fullscreen_window()
print(driver.title)
print(driver.current_url)

logo = driver.find_element(By.CLASS_NAME, "nsdq-logo--default")
logo.is_displayed()
print(logo.value_of_css_property("color"))
assert logo.value_of_css_property("color") == "rgba(8, 6, 42, 1)"
print(logo.value_of_css_property("font-size"))
assert logo.value_of_css_property("font-size") == "16px"

Market_Activity = driver.find_element(By.XPATH, "//span[text()='Market Activity']").text
print(Market_Activity)
assert  Market_Activity == "Market Activity"
time.sleep(2)