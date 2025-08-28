# https://rahulshettyacademy.com/dropdownsPractise/

import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

driver.maximize_window()
driver.find_element(By.ID, "autosuggest").send_keys("ind")
time.sleep(2)
#driver.find_element(By.XPATH,"//li[@class='ui-menu-item']/a[text()='India']").click()
countries = driver.find_elements(By.XPATH,"//li[@class='ui-menu-item']/a")
print(f"Length of Countries is: {len(countries)}")

country_names=[]

for country in countries:
    if country.text == "Indonesia":
        country.click()
        break
    else:
        country_names.append(country.text)

assert driver.find_element(By.ID, "autosuggest").get_attribute("value") == "Indonesia"

print(country_names)
for name in country_names:
    print(f"Countries present in dropdown are: {name}")



