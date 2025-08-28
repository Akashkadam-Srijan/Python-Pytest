import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.implicitly_wait(4)

# 1. Check shop button is clickable
driver.find_element(By.LINK_TEXT,"Shop").click()

# 2. Select product from list
mobile_product = driver.find_elements(By.XPATH,"//div[@class='card h-100']")
for mobile in mobile_product:
    mobile_name=mobile.find_element(By.XPATH,"div/h4/a").text
    print(f"Mobile Names:{mobile_name}")
    if mobile_name == "Blackberry":
        mobile.find_element(By.XPATH,"div/button").click()

# 3. Click on Checkout button
checkout_button = driver.find_element(By.CSS_SELECTOR,"a[class*='btn-primary']")
print("Background-color",checkout_button.value_of_css_property("background-color"))
print("Color",checkout_button.value_of_css_property("color"))
print("Font-size",checkout_button.value_of_css_property("font-size"))
print(checkout_button.text)
assert checkout_button.is_displayed()
if checkout_button.is_displayed():
    checkout_button.click()

# 4. Click on Checkout for confirm order
confirm_checkout = driver.find_element(By.XPATH,"//button[@class = 'btn btn-success']")
print("Background-color",confirm_checkout.value_of_css_property("background-color"))
print("Color",confirm_checkout.value_of_css_property("color"))
print("Font-size",confirm_checkout.value_of_css_property("font-size"))
print("Font-size",confirm_checkout.value_of_css_property("font-weight"))
if confirm_checkout.is_displayed():
    confirm_checkout.click()

# 5. Select delivery location

driver.find_element(By.XPATH,"//input[@id='country']").send_keys("Ind")
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//a[text()='India']")))
driver.find_element(By.XPATH,"//a[text()='India']").click()

# 6. Click on Purchase
driver.find_element(By.CSS_SELECTOR,"div[class='checkbox checkbox-primary']").click()
submit_Button = driver.find_element(By.CSS_SELECTOR,"input[class*='success btn-lg']")
print("Background-color",submit_Button.value_of_css_property("background-color"))
print("Color",submit_Button.value_of_css_property("color"))
print("Font-size",submit_Button.value_of_css_property("font-size"))
print("Font-size",submit_Button.value_of_css_property("font-weight"))
if submit_Button.is_displayed():
    submit_Button.click()

# 7. Verify success MSG
success_msg = driver.find_element(By.CSS_SELECTOR,"div[class*='alert-success']").text
print(success_msg)
assert "Success! Thank you!" in success_msg






